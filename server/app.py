# app.py

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from internals.models.models_manager import ModelsManager
from server.internals.api.configure_routes import configure_routes

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

configure_routes(app)

models_manager = ModelsManager()

routes = Api(app)
jwt = JWTManager(app)

routes.add_resource(Routes, '/products')

if __name__ == '__main__':
    app.run(debug=True)
