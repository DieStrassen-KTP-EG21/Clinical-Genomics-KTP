from GA import db
from GA.models.doctor import Doctor
from GA.models.patient import Patient


class Report(db.Model):
    ReportNo=db.Column(db.Integer,nullable=False,primary_key=True)
    DoctorID=db.Column(db.Integer,nullable=False)
    DoctorName=db.Column(db.String(50), nullable=False)
    PatientName=db.Column(db.String(50), nullable=False)
    PatientID=db.Column(db.Integer,nullable=False)
    ComparisonResult=db.Column(db.String(1000),nullable=False)

    def __repr__(self):
        return f"Report\n Report Number: '{self.ReportNo}',\n DoctorName: '{self.DoctorName}' \n PatientName: '{self.PatientName}' \n ComparisonResult: '{self.ComparisonResult}'\n---------------\n)"

    def __init__(self,number,doc,patient,result):
        self.ReportNo=number
        #This doctor object has their name passed to DoctorName in db column
        self.Doctor=doc
        #same with patient
        self.Patient=patient
        #result is yet to be made system analyzer
        self.Result=result
