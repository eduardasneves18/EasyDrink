from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect, render
from services import category


class AboutPageView(TemplateView):
    template_name = 'about.html'


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactsPageView(TemplateView):
    template_name = 'contacts.html'


class CartView(TemplateView):
    template_name = 'cart/cart_detail.html'


class WishesPageView(TemplateView):
    template_name = 'wishes_list.html'


class UserPageView(TemplateView):
    template_name = 'user/login.html'