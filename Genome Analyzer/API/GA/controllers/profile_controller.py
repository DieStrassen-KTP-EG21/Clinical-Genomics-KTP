from flask import jsonify

def get_profile(current_user):
	return jsonify(Name=current_user.Name, ID=current_user.ID, Gender=current_user.Gender, Phone=current_user.Phone,
		Address=current_user.Address, Email=current_user.Email, EmployeeType=current_user.EmployeeType)