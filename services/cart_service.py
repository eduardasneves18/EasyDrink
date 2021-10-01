import requests
from carts.models import User

def get_cart(request, userID):
    url = 'http://127.0.0.1:8000/api/v1/carts/checkout/{}'.format(userID)
    response = requests.get(url)
    return response.json()




