from flask_restful import Resource, reqparse
from flask import Request

sign_up_args = reqparse.RequestParser()
sign_up_args.add_argument("Name", type=str, help="Name is required", required=True)
sign_up_args.add_argument("Gender", type=str, help="Gender is required", required=True)
sign_up_args.add_argument("L", type=list, help="x is required", required=True)

class Sign_up(Resource):
	def post(self):
		args = sign_up_args.parse_args()
		return args