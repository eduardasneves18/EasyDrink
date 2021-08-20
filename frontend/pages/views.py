from django.views.generic import TemplateView


class AboutPageView(TemplateView):
    template_name = 'about.html'


class HomePageView(TemplateView):
    template_name = 'home.html'


class ProdutoView(TemplateView):
    template_name = 'products/products_list.html'


class ProductsDetailView(TemplateView):
    template_name = 'products/product_detail.html'
