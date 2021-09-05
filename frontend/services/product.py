import requests
# import json

def get_products():
    url = "http://127.0.0.1:8080/api/v1/products/"
    request = requests.get(url)
    products = request.json()
    products_list = {'products':products}
    return products_list


def get_products_by_id(pk):
    url = 'http://127.0.0.1:8080/api/v1/products/{}'.format(pk)
    request = requests.get(url)
    product = request.json()
    selectd_product = {'product':product}
    return selectd_product
