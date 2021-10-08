from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product
from services import products_service


class SearchProductView(ListView):
    template_name = "search/result_query.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')

        if query is not None:
            request = self.request
            products = products_service.get_products_search(request, query)
            context['products'] = products
            
        context['query'] = query
        return context

    def get_queryset(self, *args, **kargs):
        request = self.request
        result = request.GET
        query = result.get('q', None)  # result['q']
        if query is not None:
            products = products_service.get_products_search(request, query)
            return render(request, "search/result_query.html", context={'query': query, 'products': products})
        products = products_service.get_products(request)
        return render(request, "search/result_query.html", context={'query': query, 'products': products})
