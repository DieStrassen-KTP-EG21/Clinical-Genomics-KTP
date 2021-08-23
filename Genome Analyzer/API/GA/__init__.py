from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import jwt


# definitions
app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


# constants
DOCTOR = "Doctor"
NURSE = "Nurse"
DM = "DataManager"


# configurations
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///GA_Database.db'
app.config["SECRET_KEY"] = "12345-54321-12345"
app.config['ACCESS_TOKEN_DURATION'] =  3600              # in seconds

# importing models
from GA.models.staff import Staff


# import APIs classes here
#from GA.routes.api_template import Api_template
from GA.routes.sign_up import Sign_up
from GA.routes.login import Login



# add assign classes to endpoints here
#api.add_resource(Api_template, '/temp')
api.add_resource(Sign_up, '/signup')
api.add_resource(Login, '/login')