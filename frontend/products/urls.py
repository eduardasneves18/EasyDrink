from django.urls import path
from .views import product_list

app_name = 'products'

urlpatterns = [
    path("", product_list, name="products_list"),
    # path("procucts/<str>", ProductsDetailView.as_view(), name="products_detail")
]