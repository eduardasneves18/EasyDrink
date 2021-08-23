from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect, render
from services import category

class AboutPageView(TemplateView):
    template_name = 'about.html'


class HomePageView(TemplateView):
    template_name = 'home.html'


# class ProdutoView(TemplateView):
#     template_name = 'products/products_list.html'


# class ProductsDetailView(TemplateView):
#     template_name = 'products/product_detail.html'


# def category_list(request):
#     categories = category.get_categories()
#     return render(request, "home.html", categories)