from django.views.generic import TemplateView


class UserPageView(TemplateView):
    template_name = 'user/login.html'
    

class RegisterPageView(TemplateView):
    template_name = 'user/register.html'

class ResetPageView(TemplateView):
    template_name = 'user/reset_password.html'