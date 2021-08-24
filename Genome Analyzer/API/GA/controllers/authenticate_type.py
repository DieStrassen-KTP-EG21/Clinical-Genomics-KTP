from functools import wraps
from GA.models.staff import Staff

def authenticate_type(types):
	def auth_type(func):
		@wraps(func)
		def auth(current_user,*args, **kwargs):
			for type in types:
				if not(type == "Doctor" or type == "Nurse" or type == "DataManager"):
					return {"success": False, "err": "You passed an invalid type"}, 403
				if(current_user.EmployeeType == type):
					return func(current_user, *args, **kwargs)
			err = ""
			for type in types:
				err += f" {type} or"
			err = err[:len(err)-3]
			return {"success": False, "err": "You are not a" + err}, 403
		return auth
	return auth_type