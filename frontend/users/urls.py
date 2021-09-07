from django.urls import path
from .views import  UserPageView, RegisterPageView, ResetPageView


app_name = "users"

urlpatterns = [
    path("", UserPageView.as_view(), name="login"),
    path("register/", RegisterPageView.as_view(), name="register"),
    path("reset/", ResetPageView.as_view(), name="reset"),
]