from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.views.generic import CreateView, View
from .models import Order, Cart


# from .models import Order


# Create your views here.
class CreateOrder(CreateView):
    template_name = "orders/index.html"
    model = Order
    fields = ("address", "comment", "cart")


class CreateCart(View):
    template_name = "orders/index.html"

    def post(self, request: WSGIRequest):
        print(request.POST)
        print(request)

        return render(request, template_name=self.template_name)
