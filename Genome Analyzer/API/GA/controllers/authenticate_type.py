from functools import wraps
from GA.models.staff import Staff

def authenticate_type(type):
	def auth_type(func):
		@wraps(func)
		def auth(current_user,*args, **kwargs):
			if not(type == "Doctor" or type == "Nurse" or type == "DataManager"):
				return {"success": False, "err": "You passed an invalid type"}, 403
			if(current_user.EmployeeType != type):
				return {"success": False, "err": "You are not a " + type}, 403

			return func(*args, **kwargs)
		return auth
	return auth_type