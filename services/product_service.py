from datetime import datetime
from models.outcome_model import ApiInfo, ApiResponse
from models.product_model import Product
from models.seller_model import Seller
from services.repositories.mercado_livre_repository import MercadoLivreRepository


class ProductService:
    def __init__(self):
        self.ml_service = MercadoLivreRepository()

    #def get_daily_sells(self, sold_quantity, days_since_created) -> int:
    #    if days_since_created == 0:
    #        return sold_quantity
    #    return round(sold_quantity / days_since_created, 2)
    
    def get_daily_revenue(self, price, daily_sells) -> float:
        return round(price * daily_sells, 2)
    
    def get_month_revenue(self, price, daily_sells) -> float:
        return round(price * daily_sells * 30, 2)
   
    #def days_since_created(self, date_created) -> int:
    #    created_date = datetime.strptime(date_created, '%Y-%m-%dT%H:%M:%S.%fZ')
    #    today = datetime.today()
    #    return (today - created_date).days

    def create_product(self, product_data):
        price = product_data.get('price')
        sold_quantity = product_data.get('sold_quantity')
        total_revenue = round(price * sold_quantity, 2) if price and sold_quantity else 0
        #days_since_created = self.days_since_created(product_data.get('date_created'))
        #daily_sells = self.get_daily_sells(sold_quantity, days_since_created)

        seller_data = product_data.get('seller')
        seller = Seller(
            id=seller_data.get('id'),
            nickname=seller_data.get('nickname'),
            power_seller_status=seller_data.get('seller_reputation').get('power_seller_status'),
            address=product_data.get('seller_address').get('city').get('name')
        )

        product = Product(
            id=product_data.get('id'),
            title=product_data.get('title'),
            price=price,
            sold_quantity=sold_quantity,
            thumbnail=product_data.get('thumbnail'),
            #date_created=product_data.get('date_created'),
            total_revenue=total_revenue,
            #days_since_created=f'{days_since_created} dias',
            #daily_sells=daily_sells,
            #daily_revenue=self.get_daily_revenue(price, daily_sells),
            #month_revenue=self.get_month_revenue(price, daily_sells),
            seller_details=seller
        )
        return product

    def get_product_summary_by_name(self, product_name):
        product_search_result = self.ml_service.fetch_product_by_name(product_name)
        products = []

        for product in product_search_result['results']:
            product = self.create_product(product)
            products.append(product)

        return [product.to_dict() if isinstance(product, Product) else product for product in products] 