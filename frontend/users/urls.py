from django.urls import path
from .views import  UserPageView, RegisterPageView, ResetPageView, login_request


app_name = "users"

urlpatterns = [
    path("login/", login_request, name="login"),
    path("register/", RegisterPageView.as_view(), name="register"),
    path("reset/", ResetPageView.as_view(), name="reset"),
]