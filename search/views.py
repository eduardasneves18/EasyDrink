from django.db.models.query_utils import Q
from django.views.generic import ListView
from products.models import Product
from .models import Search
from rest_framework import viewsets
from .serializers import SearchSerializer

# Create your views here.
class SearchProductView(ListView):
    
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

    def get_queryset(self,*args,**kwargs):
        request = self.request
        result = request.GET
        query = result.get('q',None)
        if query is not None:
            return Product.Objects.search(query)
        return Product.Objects.featured() # n sei se isso ta funcionando perfeitamente 

class SearchViewSet(viewsets.ModelViewSet):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer