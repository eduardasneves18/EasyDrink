from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponsePermanentRedirect
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from rest_framework import generics, status, views, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken #token de atualização
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import RegisterSerializer, SetNewPasswordSerializer, ResetPasswordEmailRequestSerializer, EmailVerificationSerializer, LoginSerializer, LogoutSerializer
from .models import User
from .utils import Util # aqui estou importando os dados do arquivo para que exerça as funçoes lá descritas.
from .renderers import UserRenderer
import jwt
import os
import requests
import random
import string


register = False

class CustomRedirect(HttpResponsePermanentRedirect):
    allowed_schemes = [os.environ.get('APP_SCHEME'), 'http', 'https']

# modo de exibição de API genérico
class RegisterView(generics.GenericAPIView):

    # campos resposáveis por enviar as informções para serializers.py
    serializer_class = RegisterSerializer

    renderer_classes = (UserRenderer,)

    # metodo para fazer a solicitação de postagem
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user) # responsável por enviar os dados para serializer.py
        serializer.is_valid(raise_exception=True) 
        serializer.save()

        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token # onde se gera o token de acesso


        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify') # aqui recebe o link que foi revertido
        absurl = 'http://'+current_site+relativeLink+"?token="+str(token) # absolute url, aqui recebo apena o token de acesso como determinado acima
        email_body = 'Hi '+user.username + \
            '. Use the link below to verify your email \n' + absurl

        # aqui dentro desse dicionário estou definindo que o primeiro vai ser o domínio que executamos, pois o objetivo é criar um link no qual se clicka e um e-mail é enviado para a pessoa. 
        # data = {'email_body': email_body, 'to_email': user.email,
        #         'email_subject': 'Verify your email'}

        Util.send_email('Verification email', email_body, user.email)

        # Util.send_email(data) # aqui estou definindo que o email deve ser enviado, instanciando data como método estático (estatic method)

        # está retornando dados do usuário 
        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmail(views.APIView):
    serializer_class = EmailVerificationSerializer

    token_param_config = openapi.Parameter(
        'token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)


    @swagger_auto_schema(manual_parameters=[token_param_config]) # utilizado para especificar um paraqmetro manualmente.
    # método para pegar o token que foi enviado ao e-mail.
    def get(self, request):
        token = request.GET.get('token') # aqui o programa está fazendo a autenticação, identificando qual usuário esta realizando a confirmação atravez da assimilação do token.
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = User.objects.get(id=payload['user_id']) # buscando os objetos por meio da id deles.
            if not user.is_verified:
                user.is_verified = True # definindo a verificação do usuário. Esse campo não é obtido por padrão, nesse caso foi definida no 'User models'.
                user.save() 
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation link expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)



class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def generate_random_password(self):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))

    def change_password(self, password, token, uidb64):
        try: 
            url = "http://127.0.0.1:8000/api/v1/auth/password-reset-complete"
            payload = {
                "password": password,
                "token": token,
                "uidb64": uidb64,
            }
            requests.patch(url, data=payload)
            return True
        except:
            return False

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = request.data.get('email', '')

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            password = self.generate_random_password()

            if (user is not None and uidb64 is not None and token is not None):
                if self.change_password(password, token, uidb64) is True:
                    email_body = 'Hello, \n Password changes sucessful your new password is: {}'.format(password)
                else:
                    email_body = 'Hello, \n Password changes failed try again'

            Util.send_email('Reset password', email_body, user.email)
            return Response({'success': 'We have sent you a link to your e-mail with further informations !!!'}, status=status.HTTP_200_OK)
        else:
            return Response({'failed': 'E-mail not found !!!'}, status=status.HTTP_200_OK)

    


class PasswordTokenCheckAPI(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def get(self, request, uidb64, token):

        redirect_url = request.GET.get('redirect_url')

        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
           
            if not PasswordResetTokenGenerator().check_token(user, token):

                print('user', user)
                print('redirect_url', redirect_url)
                if redirect_url is not None and len(redirect_url) > 3:
                    return CustomRedirect(redirect_url+'?token_valid=False')
                else:
                    return CustomRedirect(os.environ.get('FRONTEND_URL', '')+'?token_valid=False')

            if redirect_url and len(redirect_url) > 3:
                return CustomRedirect(redirect_url+'?token_valid=True&message=Credentials Valid&uidb64='+uidb64+'&token='+token)
            else:
                return CustomRedirect(os.environ.get('FRONTEND_URL', '')+'?token_valid=False')

        except DjangoUnicodeDecodeError as identifier:
            try:
                if not PasswordResetTokenGenerator().check_token(user):
                    return CustomRedirect(redirect_url+'?token_valid=False')
                    
            except UnboundLocalError as e:
                return Response({'error': 'Token is not valid, please request a new one'}, status=status.HTTP_400_BAD_REQUEST)



class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)