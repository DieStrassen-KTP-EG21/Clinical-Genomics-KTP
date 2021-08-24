from flask import jsonify
from GA import bcrypt
from GA.models.staff import Staff
from GA import app
import jwt
import datetime


def login(name, password):
	user = Staff.query.filter_by(Name=name).first()
	if(user):
		if(bcrypt.check_password_hash(user.Password, password)):
			# Logged in
			token = jwt.encode({'public_id': user.ID, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(seconds=app.config['ACCESS_TOKEN_DURATION'])}, app.config['SECRET_KEY'], 'HS256')
			return jsonify({'access_token' : token, 'success': True}) 
		else:
			return {"success": False, "err": "wrong password"}, 403
	else:
		return {"success": False, "err": "user doesn't exist"}, 404