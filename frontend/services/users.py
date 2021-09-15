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


def register(pk):
    url = 'http://127.0.0.1:8080/auth/login/'
    request = requests.get(url)
    product = request.json()
    selectd_product = {'product':product}
    return selectd_product
