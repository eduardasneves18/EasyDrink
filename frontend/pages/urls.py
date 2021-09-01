from typing import final
from django.urls import path

from .views import AboutPageView, HomePageView, ContactsPageView, CartView, WishesPageView, UserPageView, CreateUserPageView


app_name = "pages"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contacts/", ContactsPageView.as_view(), name="contacts"),
    path("cart/", CartView.as_view(), name="cart"),
    path("wishes/", WishesPageView.as_view(), name="wishes"),
    path("login/", UserPageView.as_view(), name="login"),
    path("create_user/", CreateUserPageView.as_view(), name="create_user"),
]
