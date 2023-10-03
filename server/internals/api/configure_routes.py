from flask_restful import Api
from . import user_controller, product_controller  # Importe os controladores

def configure_routes(app):
    api = Api(app)
    
    # Rotas para usuários
    api.add_resource(user_controller.UserResource, '/users')
    api.add_resource(user_controller.UserDetailResource, '/users/<int:user_id>')
    
    # Rotas para produtos
    api.add_resource(product_controller.ProductResource, '/products')
    api.add_resource(product_controller.ProductDetailResource, '/products/<int:product_id>')
