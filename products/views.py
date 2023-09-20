from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "products/index.html")


def products_view(request):
    return render(request, "products/products.html")


def product_detail(request):
    return render(request, "products/product_detail.html")
