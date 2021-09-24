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