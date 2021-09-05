from django.urls import path
from .views import CartPageView
# from .views import cart_detail

app_name = 'carts'

urlpatterns = [
    # path("", cart_detail, name="cart"),
    path("", CartPageView.as_view(), name="cart")
]