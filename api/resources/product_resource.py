from flask_restful import Resource
from models.product_model import Product
from services.evaluator_service import ProductEvaluatorService
from services.product_service import ProductService

class ProductResource(Resource):
    def __init__(self):
        self.service = ProductService()

    def get(self, product_name):
        products = self.service.get_product_summary_by_name(product_name)

        return products
    
class ProductEvaluationResource(Resource):
    def __init__(self):
        self.service = ProductEvaluatorService()

    def get(self, product_name):
        evaluation = self.service.get_product_evaluation_by_name(product_name)
        return evaluation.to_dict()


