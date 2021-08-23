from flask import jsonify
from GA import bcrypt
from GA.models.staff import Staff


def login(name, password):
	user = Staff.query.filter_by(Name=name).first()
	if(user):
		if(bcrypt.check_password_hash(user.Password, password)):
			# Logged in
			token = ""
			return jsonify(access_token=token)
		else:
			return {"success": False, "err": "wrong password"}, 401
	else:
		return {"success": False, "err": "user doesn't exist"}, 401