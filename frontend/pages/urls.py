from django.urls import path

from .views import AboutPageView, HomePageView

#, ProdutoView, ProductsDetailView, category_list

app_name = "pages"

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
    # path("", category_list, name="home"),
    # path("products/", ProdutoView.as_view(), name="products"),
    # path("products/detail", ProductsDetailView.as_view(), name="productDetail"),

]
