from django.shortcuts import render
from services import cart
from django.views.generic import TemplateView

# def cart_detail(request):
#     selected_product = cart.get_cart
#     return render(request, "carts/cart_detail.html", selected_product)

class CartPageView(TemplateView):
    template_name = 'cart/cart_detail.html'