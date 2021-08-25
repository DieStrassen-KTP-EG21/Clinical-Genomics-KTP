from GA import db, app
from GA.models.genbank import file_names, AllRecs, compare
from GA.models.patient import Patient



def analyze_this(patientID,storedData):
    patient= Patient.query.get(patientID)
    if(patient):
        Result=compare(patient.Sequence, storedData)
        return{'success':True,'message':"Comparison Done Successfully","Result Disease ": Result['ResultDisease'],
        "Result Disease Score":Result['highscore'] ,"Disease Scores":Result['AllDiseasesScores']},200
    else:
        return{'success':False, 'err':"Patient doesn't exist in database"},404




