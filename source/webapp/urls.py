from django.contrib import admin
from django.urls import path
from .views import ProductList, ProductDetails, ProductEdit, ProductDelete

app_name = 'webapp'

urlpatterns = [
    path('', ProductList.as_view(), name='main_url'),
    path('details/<int:pk>/', ProductDetails.as_view(), name='product_details_url'),
    path('edit/<int:pk>/', ProductEdit.as_view(), name='product_edit_url'),
    path('delete/<int:pk>/', ProductDelete.as_view(), name='product_delete_url')
]