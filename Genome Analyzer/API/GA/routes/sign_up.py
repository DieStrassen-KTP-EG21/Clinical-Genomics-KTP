from flask_restful import Resource, reqparse
from GA.controllers.signup_controller import sign_up



sign_up_args = reqparse.RequestParser()
sign_up_args.add_argument("Name", type=str, help="Name is required", required=True)
sign_up_args.add_argument("Gender", type=str, help="Gender is required", required=True)
sign_up_args.add_argument("Phone", type=str, help="Phone is required", required=True)
sign_up_args.add_argument("Address", type=str, help="Address is required", required=True)
sign_up_args.add_argument("Email", type=str, help="Email is required", required=True)
sign_up_args.add_argument("Password", type=str, help="Password is required", required=True)
sign_up_args.add_argument("EmployeeType", type=str, help="EmployeeType is required", required=True)


class Sign_up(Resource): ## TODO: restrict access to sign up to be for DataManager ONLY
	
	def post(self):
		args = sign_up_args.parse_args()
		name = args["Name"]
		gender = args["Gender"]
		phone = args["Phone"]
		address = args["Address"]
		email = args["Email"]
		password = args["Password"]
		etype = args["EmployeeType"]

		return sign_up(name, email, gender, phone, address, password, etype)