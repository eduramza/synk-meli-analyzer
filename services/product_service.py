from datetime import datetime
from models.outcome_model import ApiResponse, PagingInfo
from models.product_model import Product
from models.seller_model import Seller
from services.repositories.mercado_livre_repository import MercadoLivreRepository


class ProductService:
    def __init__(self):
        self.ml_service = MercadoLivreRepository()

    def get_daily_sells(self, sold_quantity, days_since_created) -> int:
        if days_since_created == 0:
            return sold_quantity
        return round(sold_quantity / days_since_created, 2)
    
    def get_daily_revenue(self, price, daily_sells) -> float:
        return round(price * daily_sells, 2) if price and daily_sells else 0
    
    def get_month_revenue(self, price, daily_sells) -> float:
        return round(price * daily_sells * 30, 2) if price and daily_sells else 0
   
    def days_since_created(self, date_created) -> int:
        if not date_created:
            return 0
        created_date = datetime.strptime(date_created, '%Y-%m-%dT%H:%M:%S.%fZ')
        today = datetime.today()
        return (today - created_date).days

    def create_product(self, response):
        product_data = response['body']
        price = product_data.get('price')
        sold_quantity = product_data.get('sold_quantity')
        total_revenue = round(price * sold_quantity, 2) if price and sold_quantity else 0
        days_since_created = self.days_since_created(product_data.get('date_created'))
        daily_sells = self.get_daily_sells(sold_quantity, days_since_created)

        product = Product(
            id=product_data.get('id'),
            catalog_product_id=product_data.get('catalog_product_id'),
            title=product_data.get('title'),
            price=price,
            sold_quantity=sold_quantity,
            thumbnail=product_data.get('thumbnail'),
            seller_id=product_data.get('seller_id'),
            created_date=product_data.get('date_created'),
            total_revenue=total_revenue,
            days_since_created=f'{days_since_created} dias',
            daily_sells=daily_sells,
            daily_revenue=self.get_daily_revenue(price, daily_sells),
            month_revenue=self.get_month_revenue(price, daily_sells),
        )
        return product
    
    def configure_pagination(self, paging):
        return {
            'total': paging['total'],
            'offset': paging['offset'],
            'limit': paging['limit']
        }

    def get_product_summary_by_name(self, product_name, offset=0, limit=20):
        product_search_result = self.ml_service.fetch_product_by_name(product_name, offset, limit)
        products_ids = []
        #add sellers nickname to final result

        page_info = self.configure_pagination(product_search_result['paging'])

        for product_a in product_search_result['results']:
            products_ids.append(product_a.get('id'))

        products_response = self.ml_service.get_multi_products_by_id(products_ids)

        result = []
        for response in products_response:
            result.append(self.create_product(response).to_dict())

        outcome_result = ApiResponse(
            info=PagingInfo(**page_info),
            data=result
        )

        return outcome_result.to_dict()