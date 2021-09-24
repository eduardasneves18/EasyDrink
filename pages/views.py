from products.models import Product
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

class OrdersPageView(TemplateView):
    template_name = 'orders.html'


class CartPageView(TemplateView):
    template_name = 'cart/cart_detail.html'


class LoginPageView(TemplateView):
    template_name = 'user/login.html'

class RegisterPageView(TemplateView):
    template_name = 'user/register.html'

class ResetPasswordPageView(TemplateView):
    template_name = 'user/reset_password.html'

def get_products(request):
    response = requests.get('http://127.0.0.1:8000/api/v1/products/').json()
    return render (request, 'products/products_list.html', {'products':response})


def get_product_detail(request, pk):
    url = 'http://127.0.0.1:8000/api/v1/products/{}'.format(pk)
    response = requests.get(url).json()
    return render (request, 'products/product_detail.html', {'product':response})
