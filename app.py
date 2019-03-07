import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.secret_key = 'redouane'
api = Api(app)


# JWT create a new endpoint ../auth
jwt = JWT(app, authenticate, identity)


# Routing
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')


# FLASK_APP = app.py FLASK_DEBUG = 1 python -m flask run
if __name__ == "__main__":
    # mapping the db with our models:
    from db import db
    db.init_app(app)
    app.run(debug=1)
