from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from my_code.db import db

from my_code.security import authenticate, identity
from my_code.resources.user import UserRegister
from my_code.resources.item import Item, ItemList
from my_code.resources.store import Store, StoreList

new_app = Flask(__name__)
new_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
new_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
new_app.secret_key = 'jose'
api = Api(new_app)


@new_app.before_first_request
def create_tables():
    db.create_all()


# new_app.config['JWT_AUTH_URL_RULE'] = '/login'  # if you need to use /login instead of /auth
# new_app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)  # token expiration time
# new_app.config['JWT_AUTH_USERNAME_KEY'] = 'email'  # auth key name to be 'email' instead of default 'username'
jwt = JWT(new_app, authenticate, identity)  # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(new_app)
    new_app.run(port=5000, debug=True)
