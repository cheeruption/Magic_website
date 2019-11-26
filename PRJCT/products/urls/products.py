from django.contrib import admin
from django.urls import path
from products.views import (
	products,
    ProductCreateView, ProductUpdateView, ProductDeleteView,
    ProductListView, ProductDetailView,
    product_list, product_detail, product_create,
    product_update, product_delete
)


app_name = 'products'

urlpatterns = [
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='delete'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='update'),
    path('', products, name = 'products'),
    path('<int:pk>/', product_detail, name = 'detail'), #в самом запросе ищем окночание на целое число, которое фиксируем как pk
    path('create/', ProductCreateView.as_view(), name = 'create'),
]
