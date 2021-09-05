from django.views.generic import TemplateView


class UserPageView(TemplateView):
    template_name = 'user/login.html'
    

class RegisterPageView(TemplateView):
    template_name = 'user/register.html'