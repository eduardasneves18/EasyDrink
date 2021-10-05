import re
import requests

def login(email, password):
    url = "http://127.0.0.1:8000/api/v1/auth/login/"
    payload = {
        "email": email,
        "password": password
    }
    response = requests.post(url, data=payload)

    return response.json()


def register(email, password, username):
    url = "http://127.0.0.1:8000/api/v1/auth/register/"
    payload = {
        "email": email,
        "password": password,
        "username": username
    }
    response = requests.post(url, data=payload)
    
    return response.json()

def reset_password(email):
    url = "http://127.0.0.1:8000/api/v1/auth/request-reset-email/"
    payload = {
        "email": email
    }
    response = requests.post(url, data=payload)
    
    return response.json()

def save_session(request, response):
    request.session['user'] = {
        'username' : response['username'],
        'email': response['email'],
        'tokens': response['tokens']
    }

def clear_session(request):
    del request.session['user']

def access_session(request):
    if request.session.get('user'):
        return request.session.get('user')