from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db.models import base
from rest_framework_simplejwt.tokens import RefreshToken, Token


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
                  'twitter': 'twitter', 'email': 'email'}

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    featured_image = models.ImageField(null = True, blank = True, default='default.jpg') #Usuário poderá colocar foto de perfil com este
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    birth_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) #campo para saber quando um usuário foi criado, para isso usei o 'adicionar automaticamnte'.
    updated_at = models.DateTimeField(auto_now=True) # campo para saber quando fez uma atualização, para isso usei o 'automaticamente agora'.
    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))


    USERNAME_FIELD = 'email' #definindo qual vai ser o capo que vai ser utilizado para fazer o login.
    REQUIRED_FIELDS = ['username'] #designando qual campo é obrigatório 

    objects = UserManager() # aqui vamos dar o comando de como gerenciar objetos do tipo acima, instanciando a classe gerente.

    def __str__(self):
        return self.email


    # metodo utilizado para que se torne possível obter os detalhes do usuário, capaz de fazer tokens de usuários
    def tokens(self):
        refresh = RefreshToken.for_user(self) #variável para o token de atualização
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
