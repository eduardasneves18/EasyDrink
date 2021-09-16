from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages
from services import users
from .forms import LoginForm, RegisterForm
  

class ResetPageView(TemplateView):
    template_name = 'user/reset_password.html'


def login_request(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')

			user = users.login(email, password)
			if user is not None:
				print('Selected User: ', user)
				return redirect("pages:home")
			else:
				messages.error(request, email)
		else:
			print(form.errors)
	else:
		form = LoginForm()

	return render(request=request, template_name="user/login.html", context={"login_form":form})



def register_request(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("pages:home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = RegisterForm()
	return render (request=request, template_name="user/register.html", context={"register_form":form})