from typing import final
from django.urls import path
from drf_yasg import views

from .views import  HomePageView, AboutPageView, ContactsPageView, WishesPageView, OrdersPageView,  CartPageView,LoginPageView, get_products, get_product_detail, RegisterPageView, ResetPasswordPageView
from pages import views

app_name = "pages"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contacts/", ContactsPageView.as_view(), name="contacts"),
    path("wishes/", WishesPageView.as_view(), name="wishes"),
    path("orders/", OrdersPageView.as_view(), name="orders"),
    path("products/", get_products, name="products"),
    path("products/<str:pk>/",get_product_detail, name="product_detail"),
    path("cart/", CartPageView.as_view(), name="cart"),
    path("login/", LoginPageView.as_view(), name="login"),
    path("register/", RegisterPageView.as_view(), name="register"),
    path("reset-password/", ResetPasswordPageView.as_view(), name="reset-password"),
]
