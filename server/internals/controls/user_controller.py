from flask_restful import Resource
from flask_jwt_extended import jwt_required

class UserResource(Resource):
    @jwt_required()
    def get(self):
        # Lógica para listar todos os usuários
        pass

    def post(self):
        # Lógica para criar um novo usuário
        pass

class UserDetailResource(Resource):
    @jwt_required()
    def get(self, user_id):
        # Lógica para obter detalhes de um usuário por ID
        pass
    
    @jwt_required()
    def put(self, user_id):
        # Lógica para atualizar um usuário por ID
        pass

    @jwt_required()
    def delete(self, user_id):
        # Lógica para excluir um usuário por ID
        pass
