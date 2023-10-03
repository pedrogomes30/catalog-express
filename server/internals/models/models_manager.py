from models.user import User
from models.product import Product

class ModelsManager:
    def __init__(self):
        self.users = User()
        self.products = Product()
