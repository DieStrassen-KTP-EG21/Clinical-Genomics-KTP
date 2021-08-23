from GA import bcrypt, db
from GA.models.staff import Staff
import re


email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def sign_up(name, email, gender, phone, address, password, etype):
	user = Staff.query.filter_by(Name=name).first()
	if(user):
		return {"success": False, "err": "username exists"}, 409 
	else:
		if(name and email and gender and phone and address and password and etype):
			if not(name.isnumeric() or email.isnumeric() or gender.isnumeric() or address.isnumeric() or etype.isnumeric()):
				if(re.fullmatch(email_regex, email)):
					if(gender == "Male" or gender == "Female" or gender == "Custom"):
						if(etype == "Doctor" or etype == "Nurse" or etype == "DataManager"):
							hashed_pass = bcrypt.generate_password_hash(password).decode('utf-8')
							member = Staff(Name=name, Gender=gender, Email=email, Phone=phone, Address=address, EmployeeType=etype, Password=hashed_pass)
							db.session.add(member)
							db.session.commit()
							return {"success": True}, 200
						else:
							return {"success": False, "err": "employee type not valid"}, 409
					else:
						return {"success": False, "err": "gender not valid"}, 409
				else:
					return {"success": False, "err": "email not valid"}, 409
			else:
				return {"success": False, "err": "a field is numeric which is not supposed to be"}, 409
		else:
			return {"success": False, "err": "a field is empty which is not supposed to be"}, 409