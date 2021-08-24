from GA import db
from GA.models.doctor import Doctor
from GA.models.patient import Patient

class Bruh:
    x='hello'

class Report(db.Model):
    ReportNo=db.Column(db.Integer,nullable=False,primary_key=True)
    DoctorName=db.Column(db.String(50), nullable=False)
    PatientName=db.Column(db.String(50), nullable=False)
    ComparisonResult=db.Column(db.String(300),nullable=False)


    def __repr__(self):
        return f"Report\n Report Number: '{self.ReportNo}',\n DoctorName: '{self.DoctorName}' \n PatientName: '{self.PatientName}' \n ComparisonResult: '{self.ComparisonResult}'\n---------------\n)"

