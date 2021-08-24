from flask_restful import Resource, reqparse
from GA.controllers.authenticate import authenticate
from GA.controllers.authenticate_type import authenticate_type
from GA import NURSE, DM
from GA import cors


class Patient(Resource):
	@authenticate
	def get(current_user, self):
		pass

	@authenticate
	@authenticate_type([NURSE])
	def post(current_user, self):
		pass

	@authenticate
	@authenticate_type([NURSE, DM])
	def put(current_user, self):
		pass

	@authenticate
	@authenticate_type([NURSE, DM])
	def delete(current_user, self):
		pass