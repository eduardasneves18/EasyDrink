# from django.views.generic import TemplateView
from django.shortcuts import render #,get_object_or_404, redirect'''


def HomePage(request):
    return render(request, 'templates/home.html')

def AboutPage(request):
    return render (request, 'templates/about.html')
# # class HomePageView(TemplateView):
# #     template_name = 'home.html'


# # class AboutPageView(TemplateView):
# #     template_name = 'about.html'


# # class ContactsPageView(TemplateView):
# #     template_name = 'contacts.html'


# # class WishesPageView(TemplateView):
# #     template_name = 'wishes_list.html'


# # def products(request):
# #     response = requests.get('http://127.0.0.1:8000/api/v1/products/list/').json()
# #     return render (request, 'templates/products/products_list.html', {'response':response})
