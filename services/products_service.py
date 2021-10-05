import requests

def get_products(request):
    response = requests.get('http://127.0.0.1:8000/api/v1/products/')
    return response.json()


def get_product_detail(request, pk):
    url = 'http://127.0.0.1:8000/api/v1/products/{}'.format(pk)
    response = requests.get(url)
    return response.json()
    
def save_item_to_buy(request, product):
    request.session['item_to_buy'] = product

def clear_item_to_buy(request):
    if request.session.get('item_to_buy'):
        del request.session['item_to_buy']

def access_item_to_buy(request):
    if request.session.get('item_to_buy'):
        return request.session.get('item_to_buy')