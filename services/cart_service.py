from django.http import response
from django.shortcuts import redirect
import requests
from services import auth_service
from django.urls import reverse
from carts.models import Cart


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

def post_cart (request, item, quantity):
    user = auth_service.access_session(request)
    userID = auth_service.get_id_by_token(user)
    itemID = item['id']

    url = 'http://127.0.0.1:8000/api/v1/carts/'

    print('User', userID)
    print('item', item)
    print('quantity', quantity)
    
    payload = {
        "user": userID,  
        "item": itemID,
        "quantity": quantity
    }
    response = requests.post(url, data=payload)

    return response.json()

def delete_item_cart (request, pk):
    url =  'http://127.0.0.1:8000/api/v1/carts/{}'.format(pk)
    response = requests.delete(url)
    return response


def get_item_by_pk(request, pk):
    url =  'http://127.0.0.1:8000/api/v1/carts/{}'.format(pk)
    response = requests.get(url)
    return response.json()


def update_cart(request, pk, quantity):
    url =  'http://127.0.0.1:8000/api/v1/carts/{}/'.format(pk)

    payload = {
        "quantity": quantity
    }

    print('Quantity', quantity)
    print('pk', pk)
    response = requests.put(url, data=payload)
    print('response', response.json())

    return response.json()