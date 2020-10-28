from django.urls import path
from django_filters.views import FilterView
from .filters import ProductFilter

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product_register', views.product_register, name='product_register'),
    path('category_load', views.category_load, name='category_load'),
    path('product_list/', views.product_list, name='product_list'),
    path('product_detail/<product_id>/', views.product_detail, name='product_detail'),
    path('product_update/<product_id>/', views.product_update, name='product_update')
]
