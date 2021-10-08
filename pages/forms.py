from requests.models import CaseInsensitiveDict
from users.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(max_length = 200, widget = forms.EmailInput())     
    password = forms.CharField(widget = forms.PasswordInput())

class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 255, widget = forms.TextInput(), required=True)
    email = forms.EmailField(max_length = 255, widget = forms.EmailInput(), required=True) 
    password = forms.CharField(widget = forms.PasswordInput(), required=True)
    # birth_date = forms.DateField(widget = forms.DateInput(), required=True)
    # first_name = forms.CharField(max_length = 200)
    # last_name = forms.CharField(max_length = 200)
    # cpf = forms.IntegerField(max_length = 9, widget = forms.NumberInput())


    def save(self, commit=True):
            user = super(RegisterForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user

class ResetPasswordForm(forms.Form):
    email = forms.EmailField(max_length = 200, widget = forms.EmailInput())    




PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

#classe criada para adicionar opção de escolha da quantidade de produtos.
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        label = 'Quantity', choices = PRODUCT_QUANTITY_CHOICES, coerce = int
    )
    override = forms.BooleanField(
                    required = False, 
                    initial = False, 
                    widget = forms.HiddenInput
    )