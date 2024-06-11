import json
import uuid

from django.contrib.auth import get_user_model
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from .models import Order, Cart
from market.models import Product
from django.utils.timezone import now
from django.template.loader import render_to_string

# from .models import Order
User = get_user_model()


# Create your views here.
class CreateOrder(CreateView):
    template_name = "orders/index.html"
    model = Order
    fields = ("address", "comment", "cart")


class CreateCart(View):
    template_name = "orders/index.html"

    def get(self, request):
        params = request.GET
        cart_id = params['cart_id']
        return render(self.request, template_name=self.template_name, context={"mew": cart_id})

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
        # template = render_to_string(request=request, template_name=self.template_name, context={'mew': 'mew2'})

        return JsonResponse({"cart_id": random_id,
                             "redirect_url": reverse_lazy("orders:create_order")[:-1]
                             })
