# auth.py

from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from models import User

jwt = JWTManager()

@jwt.user_loader_callback
def user_loader_callback(identity):
    return User.query.get(identity)

# Crie rotas para registro, login e geração de tokens JWT
