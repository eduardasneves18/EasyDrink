from django.views.generic import ListView
from products.models import Product

# Create your views here.
class SearchProductView(ListView):

    template_name = "templates/search/result_query.html"

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
            return Product.objects.search(query) # n sei se isso ta funcionando perfeitamente 
        return Product.objects.featured() # n sei se isso ta funcionando perfeitamente 