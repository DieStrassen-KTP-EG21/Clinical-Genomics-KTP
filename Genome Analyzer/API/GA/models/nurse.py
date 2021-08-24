from GA.models.staff import Staff

class Nurse(Staff):
    def __init__(self,name,ID,gender,phone,address,email,password):
        self.Name=name
        self.ID=ID
        self.Gender=gender
        self.Phone=phone
        self.Address=address
        self.Email=email
        self.Password=password
        self.EmployeeType='Nurse'