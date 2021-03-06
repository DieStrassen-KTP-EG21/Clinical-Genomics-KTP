from operator import add
from re import A
from typing import Sequence
from flask.scaffold import F
from flask_restful import Resource, reqparse
from sqlalchemy.sql.elements import True_
from GA.controllers.authenticate import authenticate
from GA.controllers.authenticate_type import authenticate_type
from GA import NURSE, DM
from GA.controllers.patient_controller import GetPatients, SetPatient, DeletePatient, NurseUpdate, DataManagerUpdate
from GA import cors

Patient_Args = reqparse.RequestParser()
Patient_Args.add_argument(
    "Name", type=str, help="Name is required", required=True)
Patient_Args.add_argument(
    "Gender", type=str, help="Gender is required", required=True)
Patient_Args.add_argument(
    "Phone", type=str, help="Phone is required", required=True)
Patient_Args.add_argument(
    "Address", type=str, help="Address is required", required=True)
Patient_Args.add_argument("Sequence", type=str,
                          help="Sequence is required", required=True)

Patient_Args1 = reqparse.RequestParser()
Patient_Args1.add_argument(
    "ID", type=int, help="ID is required", required=True)

Patient_Args2 = reqparse.RequestParser()
Patient_Args2.add_argument("Name", type=str, required=False)
Patient_Args2.add_argument("Gender", type=str, required=False)
Patient_Args2.add_argument("Phone", type=str, required=False)
Patient_Args2.add_argument("Address", type=str, required=False)
Patient_Args2.add_argument("isApproved", type=bool, required=False)
Patient_Args2.add_argument("Sequence", type=str, required=False)
Patient_Args2.add_argument("ID", type=int, required=True)


class Patient(Resource):
    @authenticate
    def get(current_user, self):
        return GetPatients(current_user)

    @authenticate
    @authenticate_type([NURSE, DM])
    def post(current_user, self):
        Args = Patient_Args.parse_args()
        name = Args["Name"]
        gender = Args["Gender"]
        phone = Args["Phone"]
        address = Args["Address"]
        sequence = Args["Sequence"]
        return SetPatient(name, gender, phone, address, sequence)

    @authenticate
    @authenticate_type([NURSE, DM])
    def put(current_user, self):
        Args = Patient_Args2.parse_args()
        name = Args["Name"]
        gender = Args["Gender"]
        phone = Args["Phone"]
        address = Args["Address"]
        sequence = Args["Sequence"]
        id = Args["ID"]
        isapproved=Args["isApproved"]
        if(current_user.EmployeeType == NURSE):
            return NurseUpdate(id, name, gender, phone, address, sequence)
        else:
            return DataManagerUpdate(id, name, gender, phone, address, sequence,isapproved)

    @authenticate
    @authenticate_type([NURSE, DM])
    def delete(current_user, self):
        Args = Patient_Args1.parse_args()
        ID = Args.ID
        return DeletePatient(ID)
