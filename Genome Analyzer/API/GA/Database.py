import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.absolute()))
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from __init__ import app
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///GA_Database.db'
db = SQLAlchemy(app)

from models import Staff






