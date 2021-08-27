from flask import jsonify
from GA import db, app
from GA.models.genbank import file_names, AllRecs, compare
from GA.models.patient import Patient



def analyze_this(patientID,storedData):
    patient= Patient.query.get(patientID)
    if(patient):
        Result=compare(patient.Sequence, storedData)
        return jsonify({'success':True,'message':"Comparison Done Successfully","Result Disease ": Result['ResultDisease'],
        "Result Disease Score":Result['HighScore'] ,"Disease Scores":Result['AllDiseasesScores']})
    else:
        return{'success':False, 'err':"Patient doesn't exist in database"},404




