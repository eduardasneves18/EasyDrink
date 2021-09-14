from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this


# class UserPageView(TemplateView):
#     template_name = 'user/login.html'    
    

class RegisterPageView(TemplateView):
    template_name = 'user/register.html'

class ResetPageView(TemplateView):
    template_name = 'user/reset_password.html'


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			if password is not None:
				return redirect("pages:home")
			else:
				messages.error(request, username)

		else:
			print('Senha correta')
            
	form = AuthenticationForm()
	return render(request=request, template_name="user/login.html", context={"login_form":form})