from django.urls import path
from .views import register_request, ResetPageView, login_request


app_name = "users"

urlpatterns = [
    path("login/", login_request, name="login"),
    path("register/", register_request, name="register"),
    path("reset/", ResetPageView.as_view(), name="reset"),
]