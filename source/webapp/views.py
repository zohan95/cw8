from django.shortcuts import render
from django.views import View


class ProductList(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'base.html')