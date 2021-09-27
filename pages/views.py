from django.contrib.auth.models import User
from products.models import Product
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from .forms import LoginForm, RegisterForm, ResetPasswordForm
from services import auth_service, products_service, cart_service
from utils import verify_is_email_reseted, verify_is_user, verify_is_user_registered, handler_login_error,handler_register_error, handler_reset_password_error

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


def get_products(request):
    response = products_service.get_products(request)
    return render(request, 'products/products_list.html', {'products': response})


def get_product_detail(request, pk):
    response = products_service.get_product_detail(request, pk)
    return render(request, 'products/product_detail.html', {'product': response})


def post_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            response = auth_service.login(email, password)

            if response is not None and verify_is_user(response):
                return redirect("pages:home")
            else:
                handler_login_error(response, form)
    else:
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
        
            print(response)
            if response is not None and verify_is_email_reseted(response):
                 return  render(request=request, template_name="user/reset_password_confirmed.html", context={"message": response['success']})
            else:
                handler_reset_password_error(response, form)
    else:
        form = ResetPasswordForm()

    return render(request=request, template_name="user/reset_password.html", context={"reset_password_form": form})




def get_cart(request):
    response = cart_service.get_cart(request, 1)
    cart = response['checkout_details']
    print('cart', cart)
    return render(request=request, template_name='cart/cart_detail.html', context={'cart': cart})