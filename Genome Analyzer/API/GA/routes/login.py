from flask_restful import Resource, reqparse
from GA.controllers.login_controller import login


login_args = reqparse.RequestParser()
login_args.add_argument("Name", type=str, help="Name is required", required=True)
login_args.add_argument("Password", type=str, help="Password is required", required=True)


class Login(Resource):

	def post(self):

		args = login_args.parse_args()
		name = args["Name"]
		password = args["Password"]

		return login(name, password)

		

		
