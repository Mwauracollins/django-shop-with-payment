from django.urls import path
from products import views

app_name = "products"

urlpatterns = [
    path('', views.index, name='homepage'),
    path('products/', views.products_view, name="products_view"),
    path('product_detail/', views.product_detail, name="product_detail"),
]