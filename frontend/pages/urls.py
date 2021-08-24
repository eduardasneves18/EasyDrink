from django.urls import path

from .views import AboutPageView, HomePageView, ContactsPageView

#, ProdutoView, ProductsDetailView, category_list

app_name = "pages"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contacts/", ContactsPageView.as_view(), name="contacts")

]
