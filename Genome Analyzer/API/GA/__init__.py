from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# definitions
app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


# configurations
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///GA_Database.db'


# importing models
from GA.models.staff import Staff


# import APIs classes here
from GA.routes.api_template import Api_template
from GA.routes.sign_up import Sign_up



# add assign classes to endpoints here
api.add_resource(Api_template, '/temp')
api.add_resource(Sign_up, '/signup')