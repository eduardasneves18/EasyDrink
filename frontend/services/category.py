import requests

def get_categories():
    url = "http://127.0.0.1:8080/api/v1/categories/"
    request = requests.get(url)
    categories = request.json()
    category_list = {'categories':categories}
    return category_list


# criado uma pasta services para colocar todas as requisiçoes que serão feitas ao backend e a serviços terceiros

# Criado o metodo get_categories

# Utiliza a biblioteca requests, para fazer requisições http GET/POST/UPDATE/DELETE

# criar a url de acesso URL BASE (HTTPS://127.0.0.1:PORT) + endpoint do servivco: (API/V1/CATEGORIES)

# guardar a requesição 'requests.get(url) em um parâmetro aqui no caso utilizei o parâmetro 'request'

# criar uma váriavel para retornar o retorno da requisição em json  'categories'

# criar a variavel para dar o retonro final     category_list = {'categories':categories}