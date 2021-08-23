from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///GA_Database.db'
api = Api(app)
db = SQLAlchemy(app)


#importing models
from GA.models.staff import Staff


# import APIs classes here
from GA.routes.api_template import Api_template




# add assign classes to endpoints here
api.add_resource(Api_template, '/temp')