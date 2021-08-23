import jwt
from functools import wraps
from GA import app
from GA.models.staff import Staff
from flask import request, jsonify

def authenticate(func):
	@wraps(func)
	def auth(*args, **kwargs):
		token = None
		if 'x-access-token' in request.headers:
			token = request.headers['x-access-token']

		if not token:
			return {'success': False, "err": 'a valid token is missing'}, 401

		try:
			data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
			current_user = Staff.query.filter_by(ID=data['public_id']).first()

		except:
			return {'success': False, 'err': 'token is invalid'}, 401

		return func(current_user, *args, **kwargs)
	return auth