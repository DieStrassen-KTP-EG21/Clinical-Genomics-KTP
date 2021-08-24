from flask_restful import Resource
from GA.controllers.authenticate import authenticate
from GA.controllers.profile_controller import get_profile

class Profile(Resource):
	@authenticate
	def get(current_user, self):
		return get_profile(current_user)