# import requests

# def get_cart():
#     url = "http://127.0.0.1:8080/api/v1/cart/"
#     request = requests.get(url)
#     carts = request.json()
#     cart = {'products':products}  #não sei o que colocar
#     return cart



#urls cart 
# from django.urls import path
# from .views import cart_detail

# app_name = 'carts'

# urlpatterns = [
#     path("", cart_detail, name="cart"),
# ]




#views cart 
# from django.shortcuts import render
# from services import cart

# def cart_detail(request):
#     selected_product = cart.get_cart
#     return render(request, "carts/cart_detail.html", selected_product)



# urls frontend app geral
#path('pcarts/', include("carts.urls"))