from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)


# import APIs classes here
from GA.routes.Api_template import Api_template




# add assign classes to endpoints here
api.add_resource(Api_template, '/temp')