from django.urls import path

from .views import AboutPageView, HomePageView, ContactsPageView, CartView

# , ProdutoView, ProductsDetailView, category_list

app_name = "pages"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contacts/", ContactsPageView.as_view(), name="contacts"),
    path("cart/", CartView.as_view(), name="cart"),

]
