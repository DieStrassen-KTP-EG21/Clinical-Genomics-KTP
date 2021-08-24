from GA import db

class Patient(db.Model):
    Name= db.Column(db.String(50),nullable=False)
    ID=db.Column(db.Integer, nullable= False, primary_key=True )
    Gender= db.Column(db.String(50),nullable=False)
    Phone= db.Column(db.String(50),nullable=False)
    Address= db.Column(db.String(80),nullable=False)
    isSeen= db.Column(db.Boolean,nullable=False,default=False)
    isApproved= db.Column(db.Boolean,nullable=False,default= False)

    def __init__(self,name,ID,gender,phone,address):
        self.Name=name
        self.ID=ID
        self.Gender=gender
        self.Phone=phone
        self.Address=address
        self.isSeen=False
        self.isApproved=False
        