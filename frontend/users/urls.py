from django.urls import path
from .views import  UserPageView, RegisterPageView


app_name = "users"

urlpatterns = [
    path("", UserPageView.as_view(), name="login"),
    path("register/", RegisterPageView.as_view(), name="register"),
]