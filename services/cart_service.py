import requests
from services import auth_service


def get_cart(request):
    # access_token = auth_service.access_session(request)

    # if access_token is not None: 
        url = 'http://127.0.0.1:8000/api/v1/carts/checkout'
        response = requests.get(url )
        return response.json()

def get_cart(request, userID):
    url = 'http://127.0.0.1:8000/api/v1/carts/checkout/{}'.format(userID)
    response = requests.get(url)
    return response.json()



