from django.shortcuts import redirect
import requests
from services import auth_service
from django.urls import reverse


def get_cart(request):
    session = auth_service.access_session(request)

    if session is not None:
        access_token = session['tokens']['access']
        header_authorization = {'Authorization': 'Bearer ' + access_token}
        url = 'http://127.0.0.1:8000/api/v1/carts/checkout'
        response = requests.get(url, headers=header_authorization)
        return response.json()
    else:
        return {
            'error_login': "not logged"
        }

