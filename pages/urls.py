from typing import final
from django.urls import path
from drf_yasg import views

# from .views import AboutPageView, HomePageView, ContactsPageView, WishesPageView
from pages import views

app_name = "pages"

urlpatterns = [
    # path("", HomePageView.as_view(), name="home"),
    # path("about/", AboutPageView.as_view(), name="about"),
    # path("contacts/", ContactsPageView.as_view(), name="contacts"),
    # path("wishes/", WishesPageView.as_view(), name="wishes"),
    path('', views.HomePage, name = 'home'),
    # path("", views.products, name="products"),
]
