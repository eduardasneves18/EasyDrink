  from django import forms


# from django.shortcuts import render, redirect

class RegisterForm(forms.Form):
    # first_name = forms.CharField(max_length = 200)
    # last_name = forms.CharField(max_length = 200)
    # cpf = forms.IntegerField(max_length = 9, widget = forms.NumberInput())
    username = forms.CharField(max_length = 255, widget = forms.TextInput())
    email = forms.EmailField(max_length = 255, widget = forms.EmailInput()) 
    birth_date = forms.DateField(widget = forms.DateInput())
    password = forms.CharField(widget = forms.PasswordInput())


    

