from flask_restful import Resource, reqparse
from GA.controllers.authenticate import authenticate
from GA.controllers.authenticate_type import authenticate_type
from GA.controllers.system_analyzer_controller import analyze_this
from GA import DOCTOR
from GA import cors
from GA.models.genbank import *



analyzer_args = reqparse.RequestParser()
analyzer_args.add_argument("PatientID", type=str,required=True)

class Analyzer(Resource):
	@authenticate
	@authenticate_type([DOCTOR])
	def get(current_user, self):
		args = analyzer_args.parse_args()
		patientID= args["PatientID"]
		return analyze_this(patientID,AllRecs)
