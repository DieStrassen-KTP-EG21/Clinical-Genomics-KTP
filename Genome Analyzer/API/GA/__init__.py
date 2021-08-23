from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from datetime import timedelta


# definitions
app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# configurations
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///GA_Database.db'
app.config["JWT_SECRET_KEY"] = "4389573498057349857897230984723"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=10)

# importing models
from GA.models.staff import Staff


# import APIs classes here
from GA.routes.api_template import Api_template
from GA.routes.sign_up import Sign_up
from GA.routes.login import Login



# add assign classes to endpoints here
api.add_resource(Api_template, '/temp')
api.add_resource(Sign_up, '/signup')
api.add_resource(Login, '/login')