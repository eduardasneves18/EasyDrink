import requests
from carts.models import User

def get_cart(request, userId):
    url = 'http://127.0.0.1:8000/api/v1/carts/checkout/{}'.format(userId)
    response = requests.get(url)
    return response.json()
