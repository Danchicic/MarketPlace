from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from .models import Shop, Product


class CreateShopView(CreateView):
    model = Shop
    success_url = 'market:index'
    template_name = 'shops/create_shop.html'


# Create your views here.
class CatalogView(View):
    template_name = "market/index.html"

    def get(self, request):
        shops = Shop.objects.all()[:10]
        context = {
            'title': "Все товары",
            "shops": shops
        }
        return render(request, self.template_name, context)


class ShopView(View):
    template_name = 'market/shop_view.html'

    def get(self, request, shop_address):
        shop = Shop.objects.select_related("review").get(address=shop_address)
        shop.views_count += 1
        shop.save()
        shop_items = Product.objects.filter(shop_id=shop.id)
        context = {'title': shop.name, 'shop': shop, 'shop_items': shop_items}
        return render(request, self.template_name, context)
