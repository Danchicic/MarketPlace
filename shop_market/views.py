from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

from django.views import View


def is_in_shop_group(user):
    return user.groups.filter(name='shop').exists()


class ShopView(View):
    # @method_decorator(user_passes_test(is_in_shop_group))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ShopIndexView(ShopView):
    template_name = 'shop/index.html'

    def get(self, request):
        return render(request, self.template_name)


class ShopOrdersView(ShopView):
    template_name = "orders/user_orders.html"

    def get(self, request):
        shop_id = request.user.id
        print(shop_id)
        return render(request, self.template_name)
