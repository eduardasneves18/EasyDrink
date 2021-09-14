  
from django import forms
from django.shortcuts import render, redirect

class LoginForm(forms.Form):
    email = forms.EmailField(max_length = 200)     
    password = forms.CharField(widget = forms.PasswordInput())