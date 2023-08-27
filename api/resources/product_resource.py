from flask_restful import Resource
from models.product_model import Product
from services.evaluator_service import ProductEvaluatorService
from services.product_service import ProductService
from flask import request

class ProductResource(Resource):
    def __init__(self):
        self.service = ProductService()

    def get(self, product_name):
        offset = int(request.args.get('offset', 0))
        limit = int(request.args.get('limit', 20))
        limit = min(limit, 20) 
        products = self.service.get_product_summary_by_name(product_name, offset, limit)

        return products
    
class ProductEvaluationResource(Resource):
    def __init__(self):
        self.service = ProductEvaluatorService()

    def get(self, product_name):
        evaluation = self.service.get_product_evaluation_by_name(product_name)
        return evaluation.to_dict()


