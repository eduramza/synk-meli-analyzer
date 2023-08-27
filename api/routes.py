from flask import Blueprint
from . import api
from .resources.product_resource import ProductEvaluationResource, ProductResource

api_blueprint = Blueprint('api', __name__)
api.init_app(api_blueprint)

api.add_resource(ProductResource, '/product/list/<string:product_name>')
api.add_resource(ProductEvaluationResource, '/product/evaluation/<string:product_name>')
