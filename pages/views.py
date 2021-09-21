from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect, render
import requests


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactsPageView(TemplateView):
    template_name = 'contacts.html'


class WishesPageView(TemplateView):
    template_name = 'wishes_list.html'

class ProductsPageView(TemplateView):
    template_name = 'products/products_list.html'

class ProductDetailPageView(TemplateView):
    template_name = 'products/product_detail.html'

class CartPageView(TemplateView):
    template_name = 'cart/cart_detail.html'

class LoginPageView(TemplateView):
    template_name = 'user/login.html'

def get_products(request):
    response = requests.get('http://127.0.0.1:8000/api/v1/products/list/').json()
    return render (request, 'products/products_list.html', {'products':response})
