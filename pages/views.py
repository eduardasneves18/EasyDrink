
from django.contrib.auth.models import User
import products
from products.models import Product

from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from .forms import LoginForm, RegisterForm, ResetPasswordForm, CartAddProductForm
from services import auth_service, products_service, cart_service
from utils import verify_is_email_reseted, verify_is_user, verify_is_user_registered, handler_login_error,handler_register_error, handler_reset_password_error


class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContactsPageView(TemplateView):
    template_name = 'contacts.html'

class WishesPageView(TemplateView):
    template_name = 'wishes_list.html'

class OrdersPageView(TemplateView):
    template_name = 'orders.html'

class LoginCartPageView(TemplateView):
    template_name = 'user/login_cart.html'
    

def home_page(request):    
    data = Product.objects.all().values    
    response = auth_service.access_session(request)
    return render(request, 'home.html', {'user': response, 'data': data})

def get_products(request):
    response = products_service.get_products(request)
    product = Product.objects.all().values
    return render(request, 'products/products_list.html', {'products': response, 'product': product})


def get_product_detail(request, pk):
    response = products_service.get_product_detail(request, pk)
    products_service.save_item_to_buy(request, response)
    return render(request, 'products/product_detail.html', {'product': response})


def post_login(request, page=None):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            response = auth_service.login(email, password)

            if response is not None and verify_is_user(response):
                auth_service.save_session(request, response)
                if page is None:
                    return redirect("pages:home")
                else:
                    return redirect(page)
            else:
                handler_login_error(response, form)
    else:
        auth_service.clear_session(request)
        form = LoginForm()

    return render(request=request, template_name="user/login.html", context={"login_form": form})


def post_register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            username = form.cleaned_data.get('username')
            response = auth_service.register(email, password, username)
        
            if response is not None and verify_is_user_registered(response):
                return  render(request=request, template_name="user/verify_email.html", context={"register_form": form})
            else:
                handler_register_error(response, form)
    else:
        form = RegisterForm()

    return render(request=request, template_name="user/register.html", context={"register_form": form})


def post_reset_password(request):
    if request.method == "POST":
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            response = auth_service.reset_password(email)
        
            if response is not None and verify_is_email_reseted(response):
                 return  render(request=request, template_name="user/reset_password_confirmed.html", context={"message": response['success']})
            else:
                handler_reset_password_error(response, form)
    else:
        form = ResetPasswordForm()

    return render(request=request, template_name="user/reset_password.html", context={"reset_password_form": form})


def get_cart(request):
    response = cart_service.get_cart(request)

    if response is not None:
        if 'error_login' not in response:
            cart = response['checkout_details']

            return render(request=request, template_name="cart/cart_detail.html", context={'cart': cart})
        else:
            return redirect('pages:login_cart')
    else: 
        return render(request=request, template_name="cart/cart_detail.html")


def add_cart(request):
    if request.method == "POST":

        response = cart_service.post_cart(request.POST)
    return render(request=request, template_name="cart/cart_detail.html")


def buy(request):
    product = products_service.access_item_to_buy(request)
    # products_service.clear_item_to_buy(request)
    if request.method == "POST":
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data.get('quantity')
            response = cart_service.post_cart(quantity)
            return  render(request=request, template_name="cart/cart_add_detail.html", context={"message": response['success']})  
    else:
        form = CartAddProductForm()    
    return render(request=request, template_name="cart/cart_add_detail.html", context={'cart_add_detail': form, 'product': product})    



