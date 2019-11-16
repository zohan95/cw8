from django.contrib import admin
from django.urls import path
from .views import ProductList

app_name = 'webapp'

urlpatterns = [
    path('', ProductList.as_view(), name='main_url')
]