import requests

def get_products():
    url = "http://127.0.0.1:8080/api/v1/products/"
    request = requests.get(url)
    products = request.json()
    products_list = {'products':products}
    return products_list
