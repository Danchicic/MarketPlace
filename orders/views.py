import json
import uuid

from django.contrib.auth import get_user_model
from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from django.utils.timezone import now

from .models import Order, Cart
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
                cart_id=form.cleaned_data['cart_id'],
                address=form.cleaned_data['address'],
                country=form.cleaned_data['country']
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

    def get(self, request):
        params = request.GET
        cart_id = params['cart_id']
        products = Cart.objects.select_related("product").filter(cart_id=cart_id)
        total = products.aggregate(Sum('product__price'))['product__price__sum']
        return render(request, template_name=self.template_name,
                      context={"form": self.form_class, "products": products, 'total_cost': total})

    @staticmethod
    def post(request):
        user_cart = json.loads(request.body.decode())
        random_id = uuid.uuid4()
        date_create = now()
        cart_objects_to_create = [
            Cart(
                user=User.objects.get(id=request.user.id),
                product=Product.objects.get(
                    id=int(el['product_id'])
                ),
                cart_id=random_id,
                date_create=date_create
            )
            for el in user_cart
        ]
        Cart.objects.bulk_create(cart_objects_to_create)
        return JsonResponse({"cart_id": random_id,
                             "redirect_url": reverse_lazy("orders:create_order")[:-1]
                             })


class UserOrders(View):
    pass
