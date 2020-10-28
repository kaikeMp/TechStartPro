from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product_register', views.product_register, name='product_register'),
    path('load_categories', views.load_categories, name='load_categories'),
    path('product_list/', views.product_list, name='product_list'),
    path('product_detail/<product_id>/', views.product_detail, name='product_detail')
]
