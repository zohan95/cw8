from django.contrib import admin
from django.urls import path
from .views import ProductList, ProductDetails, ProductEdit, ProductDelete, ProductCreate, ReviewCreate, ReviewEdit, ReviewDelete

app_name = 'webapp'

urlpatterns = [
    path('', ProductList.as_view(), name='main_url'),
    path('details/<int:pk>/', ProductDetails.as_view(), name='product_details_url'),
    path('edit/<int:pk>/', ProductEdit.as_view(), name='product_edit_url'),
    path('delete/<int:pk>/', ProductDelete.as_view(), name='product_delete_url'),
    path('create/', ProductCreate.as_view(), name='product_create_url'),
    path('review/create/<int:pk>/', ReviewCreate.as_view(), name='review_create_url'),
    path('review/edit/<int:pk>/', ReviewEdit.as_view(), name='review_edit_url'),
    path('review/delete/<int:pk>/<int:id>/', ReviewDelete.as_view(), name='review_delete_url')
]