from GA import db
from GA.models.doctor import Doctor
from GA.models.patient import Patient


class Report(db.Model):
    ID=db.Column(db.Integer,nullable=False,primary_key=True)
    DoctorID=db.Column(db.Integer,nullable=False)
    PatientID=db.Column(db.Integer,nullable=False)
    Result=db.Column(db.String(1000),nullable=False)

    def __repr__(self):
        return f"Report\n Report Number: '{self.ReportNo}',\n DoctorName: '{self.DoctorName}' \n PatientName: '{self.PatientName}' \n ComparisonResult: '{self.ComparisonResult}'\n---------------\n)"

    def __init__(self,docID,patientID,result):
        #This doctor object has their name passed to DoctorName in db column
        self.DoctorID=docID
        #same with patient
        self.PatientID=patientID
        #result is yet to be made by the doctor
        self.Result=result
