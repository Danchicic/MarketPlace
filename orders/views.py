import json
import uuid

from django.contrib.auth import get_user_model
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from django.utils.timezone import now

from .models import Order, Cart, CartProduct
from market.models import Product
from .forms import CreateOrderForm

User = get_user_model()


# Create your views here.
class CreateOrder(CreateView):
    model = Order
    fields = ('name', 'address', 'country', 'cart')
    template_name = "orders/index.html"

    def post(self, request, *args, **kwargs):
        form_body = json.loads(request.body.decode())
        form: CreateOrderForm = CreateOrderForm(form_body)
        form_errors = form.errors.as_data()

        if form.is_valid():
            new_order = Order(
                name=form.cleaned_data['name'],
                cart=Cart.objects.get(id=form.cleaned_data['cart_id']),
                address=form.cleaned_data['address'],
                country=form.cleaned_data['country'],
                user=User.objects.get(id=request.user.id)
            )

            new_order.save()
            return JsonResponse({"success": True})
        elif form_errors:
            print("some errors in form", form_errors)

            if form_errors.get('name') or form_errors.get('address') or form_errors.get('country'):
                return JsonResponse({"message": "Fill all fields", "code": 0})

            elif form_errors.get('cart_id'):
                return JsonResponse({"message": "Your order is already created", "code": -1})
            return JsonResponse(form_errors)


class CreateCart(View):
    template_name = "orders/index.html"
    form_class = CreateOrderForm()

    @staticmethod
    def post(request):
        # get user cart data from form
        user_cart = json.loads(request.body.decode())
        new_user_cart_object = Cart(
            user=User.objects.get(id=request.user.id)
        )

        cart_product_objects_to_create = [
            CartProduct(
                cart=new_user_cart_object,
                product=Product.objects.get(
                    id=int(el['product_id'])
                ),
            )
            for el in user_cart
        ]
        new_user_cart_object.save()
        CartProduct.objects.bulk_create(cart_product_objects_to_create)
        return JsonResponse({"cart_id": new_user_cart_object.id,
                             "redirect_url": reverse_lazy("orders:create_order")[:-1]
                             })

    def get(self, request):
        params = request.GET
        cart_id = params['cart_id']
        products = CartProduct.objects.filter(cart_id=cart_id)
        total = products.aggregate(Sum('product__price'))['product__price__sum']

        return render(request, template_name=self.template_name,
                      context={"form": self.form_class, "products": products, 'total_cost': total})


class UserOrders(View):
    template_name = 'orders/user_orders.html'

    def get(self, request):
        user_orders = Order.objects.prefetch_related(
            'cart',
            'cart__cartproduct_set',
            'cart__cartproduct_set__product'
        ).filter(
            user_id=request.user.id
        ).annotate(
            total_price=Sum('cart__cartproduct__product__price')
        )

        context = {
            "user_orders": user_orders
        }

        return render(request, self.template_name, context=context)
