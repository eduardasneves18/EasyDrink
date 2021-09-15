from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
# from django.shortcuts import render, redirect

class LoginForm(forms.Form):
    email = forms.EmailField(max_length = 200, widget = forms.EmailInput())     
    password = forms.CharField(widget = forms.PasswordInput())


class RegisterForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(RegisterForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user