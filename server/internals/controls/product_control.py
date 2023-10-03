from flask_restful import Resource

class ProductResource(Resource):
    def get(self):
        # Lógica para listar todos os produtos
        pass

    def post(self):
        # Lógica para criar um novo produto
        pass

class ProductDetailResource(Resource):
    def get(self, product_id):
        # Lógica para obter detalhes de um produto por ID
        pass

    def put(self, product_id):
        # Lógica para atualizar um produto por ID
        pass

    def delete(self, product_id):
        # Lógica para excluir um produto por ID
        pass
