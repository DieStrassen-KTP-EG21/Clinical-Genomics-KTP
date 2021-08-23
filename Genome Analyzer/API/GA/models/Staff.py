import sys
sys.path.append("..")
from GA import db
class Staff(db.Model):
    Name= db.Column(db.String(50),nullable=False)
    ID = db.Column(db.Integer, primary_key=True, nullable=True)
    Gender= db.Column(db.String(50),nullable=False)
    Phone= db.Column(db.Integer,nullable=True)
    Address= db.Column(db.String(50),nullable=True)
    Email= db.Column(db.String(50),nullable=True)
    Password= db.Column(db.String(50),nullable=True)
    Employee= db.Column(db.String(50),nullable=True)


    def __repr__(self):
        return f"Staff('{self.Name}', '{self.Gender}')"



