import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.absolute()))
from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)




# import APIs classes here
from routes.Api_template import Api_template



# add assign classes to endpoints here
api.add_resource(Api_template, '/temp')