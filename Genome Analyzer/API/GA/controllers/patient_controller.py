from operator import add
from re import S
from typing import Sequence
from flask import jsonify
from flask.scaffold import F
from GA import bcrypt
from GA.models.patient import Patient
from GA import  DM
from GA import bcrypt, db
from GA import app


def IsGenderValid(gender):
    return gender in {"Male", "Female", "Custom"}


def IsSequenceValid(seq):
    return next((gene for gene in seq if gene not in ['T', 'C', 'G', 'A']), None) == None


def IsNotNone(item):
    return item is not None


def GetPatients(current_user):
    Data = []
    users = Patient.query.all()
    for user in users:
        dic = {
            "Name": user.Name,
            "ID": user.ID,
            "Gender": user.Gender,
            "Phone": user.Phone,
            "Address": user.Address,
            "isApproved": user.isApproved,
            "Sequence": user.Sequence
        }
        if(current_user.EmployeeType==DM):
            dic["isSeen"]=user.isSeen
        Data.append(dic)
    if users:
        return {"success": True, "Patients": Data}, 200
    else:
        return {"success": False, "err": "No patients exist "}, 404


def SetPatient(name, gender, phone, address, sequence):
    user = Patient.query.filter_by(Name=name).first()
    lst = [name, gender, phone, sequence,address]
    if(user):
        return {"success": False, "err": "username exists"}, 409

    for element in lst:
        if not IsNotNone(element):
            return {"success": False, "err": "a field is empty which is not supposed to be"}, 409

    for element in lst:
        if element.isnumeric() and element != phone:
            return {"success": False, "err": "a field is numeric which is not supposed to be"}, 409

    if(not IsGenderValid(gender)):
        return {"success": False, "err": "gender not valid"}, 409

    if(not IsSequenceValid(sequence)):
        return {"success": False, "err": "Sequence is not valid"}, 409

    member = Patient(name, gender, phone, address, sequence)
    db.session.add(member)
    db.session.commit()
    return {"success": True}, 200


def DeletePatient(id):
    user = Patient.query.get(id)
    try:
        db.session.delete(user)
        db.session.commit()
        return {"success": True}, 200
    except:
        return {"success": False, "Error": "User doesn't exist!"}, 404


def Update(id, name, gender, phone, address, sequence):
    user = Patient.query.filter_by(ID=id).first()
    if(name):
        if(not name.isnumeric()):
            user.Name = name
            db.session.commit()
        else : return {"success":False,"Error":"Name is not valid"}
          

    if(phone):
        if(not phone.isnumeric()):
            user.Phone = phone
            db.session.commit()
        else : return {"success":False,"Error":"Phone is not valid"}        

    if(sequence):
        if(IsSequenceValid(sequence)):
            user.Sequence = sequence
            db.session.commit()
        else : return {"success":False,"Error":"Sequence is not valid"}    


    if(gender):
        if( IsGenderValid(gender)):
            user.Sequence = sequence
            db.session.commit()
        else : return {"success":False,"Error":"Gender is not valid"}    

    if(address ):
        if( not address.isnumeeric()):
            user.address = address
            db.session.commit()
        else : return {"success":False,"Error":"Address is not valid"}    

    return {"success": True}, 200


def NurseUpdate(id, name, gender, phone, address, sequence):
    return Update(id, name, gender, phone, address, sequence)


def DataManagerUpdate(id, name, gender, phone, address, sequence,isapproved):
    p = Patient.query.filter_by(ID=id).first()  
    if(isapproved ==True or isapproved==False): 
        p.isApproved=isapproved

    if(not p):
        return {"success": False, "Error": "User doesn't exist!"}, 404

    p.isApproved=True
    db.session.commit()
    return Update(id, name, gender, phone, address, sequence)

   
