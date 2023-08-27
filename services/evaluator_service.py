from models.product_evaluation import CompetitionCounter, ProductEvaluation, SalesCounter
from services.repositories.mercado_livre_repository import MercadoLivreRepository


class ProductEvaluatorService:

    def __init__(self):
        self.ml_repository = MercadoLivreRepository()

    def get_product_evaluation_by_name(self, product_name):
        product_data = self.ml_repository.fetch_all_products_by_name(product_name)

        # Initialize variables for competition, sales summary, and prices
        competition = {"no_value": 0, "leader": 0, "gold": 0, "platinum": 0}
        sales_summary = {"minimum_qtd": float('inf'), "maximum_qtd": 0, "total": 0}
        price_range = [float('inf'), 0]  # min and max price

        status_mapping = {
            "líder": "leader",
            "gold": "gold",
            "platinum": "platinum",
            "sem reputação": "no_value"
        }

        # Iterate over all products
        for product in product_data:
            seller_details = product.get('seller', {})
            seller_reputation = seller_details.get('seller_reputation', {})
            seller_status = seller_reputation.get('power_seller_status', "sem reputação")
            competition_key = status_mapping.get(seller_status, "no_value")
            competition[competition_key] += 1

            sold_quantity = product.get('sold_quantity', 0)
            sales_summary['total'] += sold_quantity
            if sold_quantity > sales_summary["maximum_qtd"]:
                sales_summary["maximum_qtd"] = sold_quantity
            if 0 < sold_quantity < sales_summary["minimum_qtd"]:
                sales_summary["minimum_qtd"] = sold_quantity

            price = product.get('price', 0)
            if price < price_range[0]:
                price_range[0] = price
            if price > price_range[1]:
                price_range[1] = price

        # Handle the case where there are no sales
        if sales_summary["minimum_qtd"] == float('inf'):
            sales_summary["minimum_qtd"] = 0
        
        # Handle the case where there are no products found
        if price_range[0] == float('inf'):
            price_range[0] = 0

        competition = CompetitionCounter(**competition)
        sales_counter = SalesCounter(**sales_summary)

        return ProductEvaluation(competition=competition, sales=sales_counter, price_range=tuple(price_range))