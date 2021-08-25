from typing import Sequence
from Bio.Seq import Seq

from Bio.SeqRecord import SeqRecord
from GA import db

class Patient(db.Model):
    Name= db.Column(db.String(50),nullable=False)
    ID=db.Column(db.Integer, nullable= False, primary_key=True )
    Gender= db.Column(db.String(50),nullable=False)
    Phone= db.Column(db.String(50),nullable=False)
    Address= db.Column(db.String(80),nullable=False)
    isSeen= db.Column(db.Boolean,nullable=False,default=False)
    isApproved= db.Column(db.Boolean,nullable=False,default= False)
    Sequence=db.Column(db.String(3000),nullable=False)

<<<<<<< HEAD
    # def __init__(self,name,ID,gender,phone,address,seqrec):
    #     self.Name=name
    #     self.ID=ID
    #     self.Gender=gender
    #     self.Phone=phone
    #     self.Address=address
    #     self.isSeen=False
    #     self.isApproved=False
    #     self.seqrec=SeqRecord(Seq("CAGTGCTAGTCAGTATGGCTAGTCATG"), id="test")
    #     self.Sequence=seqrec.seq
        
=======
    def __init__(self,name,gender,phone,address,seqrec):
        self.Name=name
        self.Gender=gender
        self.Phone=phone
        self.Address=address
        self.isSeen=False
        self.isApproved=False
        self.Sequence=seqrec
>>>>>>> 73d5495f6bdc1d4d84e8aeabb38ae0373d88d840
