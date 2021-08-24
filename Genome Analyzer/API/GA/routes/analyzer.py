from flask_restful import Resource
from GA.controllers.authenticate import authenticate
from GA.controllers.authenticate_type import authenticate_type
from GA import DOCTOR
from GA import cors


class Analyzer(Resource):
	@authenticate
	@authenticate_type([DOCTOR])
	def get(current_user, self):
		pass
