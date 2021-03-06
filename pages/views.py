from products.models import Product
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from .forms import LoginForm, RegisterForm, ResetPasswordForm, CartAddProductForm
from services import auth_service, products_service, cart_service
from utils import verify_is_email_reseted, verify_is_user, verify_is_user_registered, handler_login_error,handler_register_error, handler_reset_password_error
from django.http.response import JsonResponse


class AboutPageView(TemplateView):
    template_name = 'about.html'
class AboutUsView(TemplateView):
    template_name = 'about_us'

class ContactsPageView(TemplateView):
    template_name = 'contacts.html'

class WishesPageView(TemplateView):
    template_name = 'wishes_list.html'

class OrdersPageView(TemplateView):
    template_name = 'orders.html'

class LoginCartPageView(TemplateView):
    template_name = 'user/login_cart.html'
    

def home_page(request):    
    data = products_service.get_products(request)  
    response = auth_service.access_session(request)
    return render(request, 'home.html', {'user': response, 'data': data})


def get_categories(request):
    return products_service.get_categories(request)


def get_products_category(request, id):
    categories = get_categories(request)
    response = products_service.get_products_by_category(request, id)
    return render(request, 'products/products_list.html', {'products': response, 'categories': categories })

def get_products(request):
    categories = get_categories(request)
    response = products_service.get_products(request)

    return render(request, 'products/products_list.html', {'products': response, 'categories': categories })


def get_product_detail(request, pk):
    product = products_service.get_product_detail(request, pk)
    if request.method == "POST":
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data.get('quantity')
            try:
                cart_service.post_cart(request, product, quantity)
            except:
                return redirect('pages:login') 
            return redirect('pages:products') 
    else:
        form = CartAddProductForm()  

    return render(request, 'products/product_detail.html', {'cart_add_detail': form, 'product': product})

def buy(request):
    product = products_service.access_item_to_buy(request)

    if request.method == "POST":
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data.get('quantity')
            response = cart_service.post_cart(request, product, quantity)
            products_service.clear_item_to_buy(request)
            return redirect('pages:products') 
    else:
        form = CartAddProductForm()    
    return render(request=request, template_name="cart/cart_add_detail.html", context={'cart_add_detail': form, 'product': product})    




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

def delete_cart(request, pk):
    cart_service.delete_item_cart(request, pk)

def increase_product_quantity(request, pk):
    product = cart_service.get_item_by_pk(request, pk)
    quantity = int(product['quantity'])

    if quantity > 0:
        quantity += 1
        cart_service.update_cart(request, pk, quantity)


def decrease_product_quantity(request, pk):
    product= cart_service.get_item_by_pk(request, pk)
    quantity = int(product['quantity'])
    if quantity > 1:
        quantity -= 1
        cart_service.update_cart(request, pk, quantity)

def get_cart(request):
    if request.method == "POST":
        if request.POST.get("delete"):
            pk = request.POST.get("delete")
            delete_cart(request, pk)
        elif request.POST.get('increase_product_quantity'):
            pk = request.POST.get("increase_product_quantity")
            increase_product_quantity(request, pk)
        elif request.POST.get('decrease_product_quantity'):
            pk = request.POST.get("decrease_product_quantity")
            decrease_product_quantity(request, pk)

    response = cart_service.get_cart(request)

    if response is not None:
        if 'error_login' not in response :
            if 'error' not in response:
                carts = response['checkout_details']
                return render(request, "cart/cart_detail.html", {'cart': carts })
            else:
                return render(request=request, template_name="cart/cart_detail.html", context={'cart': None})
        else:
            return redirect('pages:login_cart')
    else: 
        return render(request=request, template_name="cart/cart_detail.html")


## Criei esse metodo para utilizar o mesmo dicionario que armazena os produtos do carrinho para poder fazer a pagina de 
# agredecimento pela compra
 
def template_payment(request):
    if request.method == "POST":
        if request.POST.get("delete"):
            pk = request.POST.get("delete")
            delete_cart(request, pk)
        elif request.POST.get('increase_product_quantity'):
            pk = request.POST.get("increase_product_quantity")
            increase_product_quantity(request, pk)
        elif request.POST.get('decrease_product_quantity'):
            pk = request.POST.get("decrease_product_quantity")
            decrease_product_quantity(request, pk)

    response = cart_service.get_cart(request)

    if response is not None:
        if 'error_login' not in response :
            if 'error' not in response:
                carts = response['checkout_details']
                return render(request, "payments/payments.html", {'cart': carts })
            else:
                return render(request=request, template_name="payments/payments.html", context={'cart': None})
        else:
            return redirect('pages:login_cart')
    else: 
        return render(request=request, template_name="payments/payments.html")

def favorite_products(request):
    if request.method == "POST":
        if request.POST.get("delete"):
            pk = request.POST.get("delete")
            delete_cart(request, pk)
        elif request.POST.get('increase_product_quantity'):
            pk = request.POST.get("increase_product_quantity")
            increase_product_quantity(request, pk)
        elif request.POST.get('decrease_product_quantity'):
            pk = request.POST.get("decrease_product_quantity")
            decrease_product_quantity(request, pk)

    response = cart_service.get_cart(request)

    if response is not None:
        if 'error_login' not in response :
            if 'error' not in response:
                carts = response['checkout_details']
                return render(request, "products/products_favorites.html", {'cart': carts })
            else:
                return render(request=request, template_name="products/products_favorites.html", context={'cart': None})
        else:
            return redirect('pages:login_cart')
    else: 
        return render(request=request, template_name="products/products_favorites.html")

def about_us(request):
    return render(request, template_name="about_us.html") 
    


