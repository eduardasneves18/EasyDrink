from typing import final
from django.urls import path
from drf_yasg import views

from .views import  HomePageView, AboutPageView, ContactsPageView, WishesPageView, ProductsPageView, ProductsPageView, ProductDetailPageView, CartPageView,LoginPageView, get_products
from pages import views

app_name = "pages"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contacts/", ContactsPageView.as_view(), name="contacts"),
    path("wishes/", WishesPageView.as_view(), name="wishes"),
    path("products/", get_products, name="products"),
    path("product_detail/", ProductDetailPageView.as_view(), name="product_detail"),
    path("cart/", CartPageView.as_view(), name="cart"),
    path("login/", LoginPageView.as_view(), name="login"),
]
