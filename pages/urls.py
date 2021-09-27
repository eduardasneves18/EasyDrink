from django.urls import path
from .views import  HomePageView, CartPageView, AboutPageView, ContactsPageView, WishesPageView, OrdersPageView,  get_cart, get_products, get_product_detail, post_register, post_reset_password, post_login


app_name = "pages"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contacts/", ContactsPageView.as_view(), name="contacts"),
    path("wishes/", WishesPageView.as_view(), name="wishes"),
    path("orders/", OrdersPageView.as_view(), name="orders"),
    path("products/", get_products, name="products"),
    path("products/<str:pk>/",get_product_detail, name="product_detail"),
    path("cart/", get_cart, name="cart"),
    path("login/", post_login, name="login"),
    path("register/", post_register, name="register"),
    path("reset-password/", post_reset_password, name="reset-password"),
]
