from typing import Sequence
from flask_restful import Resource, reqparse
from GA.controllers.authenticate import authenticate
from GA.controllers.authenticate_type import authenticate_type
from GA import NURSE, DM
from GA.controllers.patient_controller import GetPatients,SetPatient
from GA import cors

Patient_Args = reqparse.RequestParser()
Patient_Args.add_argument("Name", type=str, help="Name is required", required=True)
Patient_Args.add_argument("Gender", type=str, help="Gender is required", required=True)
Patient_Args.add_argument("Phone", type=str, help="Phone is required", required=True)
Patient_Args.add_argument("Address", type=str, help="Address is required", required=True)
Patient_Args.add_argument("Sequence", type=str, help="Sequence is required", required=True)

class Patient(Resource):
	@authenticate
	def get(current_user,self):
		return  GetPatients()

	@authenticate
	@authenticate_type([NURSE,DM])
	def post(current_user,self):
		Args = Patient_Args.parse_args()
		name = Args["Name"]
		gender = Args["Gender"]
		phone = Args["Phone"]
		address = Args["Address"]
		sequence= Args["Sequence"]
		return  SetPatient(name,gender,phone,address,sequence)

	@authenticate
	@authenticate_type([NURSE, DM])
	def put(current_user, self):
		pass

	@authenticate
	@authenticate_type([NURSE, DM])
	def delete(current_user, self):
		pass