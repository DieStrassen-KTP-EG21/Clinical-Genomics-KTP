from operator import add
from re import S
from typing import Sequence
from flask import jsonify
from flask.scaffold import F
from GA import bcrypt
from GA.models.patient import Patient
from GA.models.nurse import Nurse
from GA import bcrypt, db
from GA import app


def GetPatients():
    Data=[]
    users=Patient.query.all()
    for user in users:
        dic={
            "Name":user.Name,
            "ID":user.ID,
            "Gender":user.Gender,
            "Phone":user.Phone,
            "Address":user.Address,
            "isApproved":user.isApproved,
            "Sequence":user.Sequence
        }
        Data.append(dic)
    if users :
     	return {"success": True,"Patients":Data}, 200
    else :return {"success":False,"err":"No patients exist "},404   



def SetPatient(name,gender,phone,address,sequence):
    user = Patient.query.filter_by(Name=name).first()
    if(user):
    	return {"success": False, "err": "username exists"}, 409 

    if(name or not gender or not phone or not address or not sequence): 
        return {"success": False, "err": "a field is empty which is not supposed to be"}, 409

    if (name.isnumeric() or sequence.isnumeric() or gender.isnumeric()):
        return {"success": False, "err": "a field is numeric which is not supposed to be"}, 409

    if(gender  not in {"Male","Female","Custom"}):
       	return {"success": False, "err": "gender not valid"}, 409 


    if(next((gene for gene in sequence if gene not in[ 'T','C','G','A']), None) != None):
        return {"success": False, "err": "Sequence is not valid"}, 409  

    member = Patient(Name=name, Gender=gender, Phone=phone, Address=address,Sequence=sequence)
    db.session.add(member)
    db.session.commit()    
    return {"success": True}, 200      

def DeletePatient(id):
    user = Patient.query.get(id) 
    try:
        db.session.delete(user)
        db.session.commit()  
        return {"success": True,"Error":"User Deleted sucessfully!"}, 200 
    except:
         return {"success": False,"Error":"User doesn't exist!"}, 404     
            
    

