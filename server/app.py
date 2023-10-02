# app.py

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from models import db
from api import ProductResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # Configure o URI do banco de dados SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Configure sua chave JWT secreta

db.init_app(app)
api = Api(app)
jwt = JWTManager(app)

api.add_resource(ProductResource, '/products')

if __name__ == '__main__':
    app.run(debug=True)
