from django.http import request
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from products.models import Product


# Create your views here.
class SearchProductView(ListView):
    def get_queryset(self,*args,**kwargs):
        request = self.request
        result = request.GET
        query = result.get('q',None)
        if query is not None:
            return Product.objects.filter(name__icontains = query)
        return get_object_or_404