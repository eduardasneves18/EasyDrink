from django.urls import path
from .views import buy, AboutPageView, ContactsPageView, WishesPageView, OrdersPageView, LoginCartPageView,  home_page, get_cart, get_products, get_product_detail, post_register, post_reset_password, post_login,template_payment


app_name = "pages"

urlpatterns = [
    path("", home_page, name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contacts/", ContactsPageView.as_view(), name="contacts"),
    path("wishes/", WishesPageView.as_view(), name="wishes"),
    path("orders/", OrdersPageView.as_view(), name="orders"),
    path("login_cart/",  LoginCartPageView.as_view(), name="login_cart"),
    path("products/", get_products, name="products"),
    path(r'^products/(?P<query>\w{0,100})/$', get_products, name="products"),
    path("products/<str:pk>/",get_product_detail, name="product_detail"),
    path("product-buy/",buy, name="buy"),
    path("cart/", get_cart, name="cart"),
    path("login/", post_login, name="login"),
    path("register/", post_register, name="register"),
    path("reset-password/", post_reset_password, name="reset-password"),
    path("payments/",template_payment, name="payments"),
]
