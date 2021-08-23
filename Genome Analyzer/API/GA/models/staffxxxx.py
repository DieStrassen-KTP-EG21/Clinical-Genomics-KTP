from GA import db


class Staff(db.Model):
    Name= db.Column(db.String(50),nullable=False, unique=True)
    ID = db.Column(db.Integer, primary_key=True, nullable=False)
    Gender= db.Column(db.String(10),nullable=False)
    Phone= db.Column(db.String(30),nullable=False)
    Address= db.Column(db.String(50),nullable=False)
    Email= db.Column(db.String(50),nullable=False)
    Password= db.Column(db.String(50),nullable=False)
    EmployeeType= db.Column(db.String(15),nullable=False)


    def __repr__(self):
        return f"Staff('{self.Name}', '{self.Gender}')"





