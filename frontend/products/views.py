from django.shortcuts import render
from services import product 

# Create your views here.

def product_list(request):
    products = product.get_products()
    return render(request, "products/products_list.html", products)