from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect, render
from services import category

class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactsPageView(TemplateView):
    template_name = 'contacts.html'

