import requests
# import json

def login(email, password):
    url = "http://127.0.0.1:8080/auth/login/"
    payload = {
        "email": email,
        "password": password
    }
    response = requests.post(url, data=payload)
    return response.json()


def register(birth_date, username, email, password):
    url = 'http://127.0.0.1:8080/auth/login/'
    payload = {
        "email": email,
        "password": password,
        "birth_date" : birth_date,
        "username" : username
    }
    response = requests.post(url, data=payload)
    return response.json()
