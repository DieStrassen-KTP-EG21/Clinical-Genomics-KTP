from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import jwt
from flask_cors import CORS


# definitions
app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
cors = CORS(app)   # you can filter origins but we will do it later    


# constants
DOCTOR = "Doctor"
NURSE = "Nurse"
DM = "DataManager"


# configurations
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///GA_Database.db'
app.config["SECRET_KEY"] = "12345-54321-12345"
app.config['ACCESS_TOKEN_DURATION'] =  43200             # in seconds

# importing models
from GA.models.staff import Staff
from GA.models.patient import Patient
from GA.models.report import Report


# import APIs classes here
from GA.routes.api_template import Api_template
from GA.routes.sign_up import Sign_up
from GA.routes.login import Login
from GA.routes.profile import Profile
from GA.routes.patient import Patient
from GA.routes.analyzer import Analyzer
from GA.routes.report import Report


# add assign classes to endpoints here
api.add_resource(Api_template, '/')
api.add_resource(Sign_up, '/signup')
api.add_resource(Login, '/login')
api.add_resource(Profile, '/profile')
api.add_resource(Patient, '/patients')
api.add_resource(Analyzer, '/analyzer')
api.add_resource(Report, '/report')