from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from webapp.models import Product


class ProductList(ListView):
    model = Product
    template_name = 'product_index.html'
    context_object_name = 'product_list'


class ProductDetails(DetailView):
    model = Product
    template_name = 'product_details.html'
    context_object_name = 'product'


class ProductEdit(UpdateView):
    model = Product
    template_name = 'product_edit.html'
    fields = ['image', 'name', 'category', 'description']
    success_url = reverse_lazy('webapp:main_url')


class ProductDelete(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('webapp:main_url')
