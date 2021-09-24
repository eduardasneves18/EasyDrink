import requests

def get_products(request):
    response = requests.get('http://127.0.0.1:8000/api/v1/products/')
    return response.json()


def get_product_detail(request, pk):
    url = 'http://127.0.0.1:8000/api/v1/products/{}'.format(pk)
    response = requests.get(url)
    return response.json()