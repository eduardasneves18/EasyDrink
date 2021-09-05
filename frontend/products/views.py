from django.shortcuts import render
from services import product 


def product_list(request):
    products = product.get_products()
    return render(request, "products/products_list.html", products)


def product_detail(request, pk):
    selected_product = product.get_products_by_id(pk)
    return render(request, "products/product_detail.html", selected_product)