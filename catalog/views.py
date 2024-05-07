from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


# Create your views here.
class DefaultView(View):
    template_name = "catalog/index.html"

    def get(self, request):
        return render(request, self.template_name, {'title': "Все товары"})
