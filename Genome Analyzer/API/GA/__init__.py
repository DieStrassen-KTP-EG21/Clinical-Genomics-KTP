from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///GA_Database.db'
api = Api(app)
db = SQLAlchemy(app)


# import APIs classes here
from routes.Api_template import Api_template




# add assign classes to endpoints here
api.add_resource(Api_template, '/temp')