import requests
import logging
from models.product_model import Product

from models.seller_model import Seller

class MercadoLivreRepository:
    BASE_URL = 'https://api.mercadolibre.com/'

    def __init__(self):
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)

    def construct_url(self, endpoint):
        url = self.BASE_URL + endpoint
        self.logger.debug(f"URL formada: {url}")
        return url

    def api_request(self, method, url, body=None):
        if method == 'GET':
            response = requests.get(url, headers=self.headers)
        elif method == 'POST':
            response = requests.post(url, headers=self.headers, json=body)
        if response.status_code != 200:
            raise Exception('Nao foi possivel realizar a operacao')
        return response.json()

    def fetch_product_by_name(self, product_name):
        endpoint = f'sites/MLB/search?q={product_name}'
        url = self.construct_url(endpoint)
        return self.api_request('GET', url)
    
    def fetch_all_products_by_name(self, product_name):
        products = []
        offset = 0
        limit = 50
        MAX_OFFSET = 950

        while True:
            endpoint = f'sites/MLB/search?q={product_name}&limit={limit}&offset={offset}'
            url = self.construct_url(endpoint)
            response = self.api_request('GET', url)

            #Assuming that response contains a list of products
            products += response['results']
            if len(response['results']) < limit or offset >= MAX_OFFSET:
                break
            offset += limit
    
        return products

