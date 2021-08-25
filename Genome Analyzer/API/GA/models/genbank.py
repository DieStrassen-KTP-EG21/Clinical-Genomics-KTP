from re import fullmatch
from Bio import SeqIO,pairwise2,Align
from Bio.pairwise2 import format_alignment
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

AllRecs=[]
<<<<<<< HEAD
file_names=["alenquer.gbk","dabiebandavirus.gbk","ebolavirus.gbk","influenza-a.gbk","hiv.gbk","sars.gbk"]

for file in file_names:
    for sq in SeqIO.parse("GA/models/disease_sequences/"+file,"genbank"):
        AllRecs.append(sq)

# sseq=Seq("CGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTA")
=======
file_names=["alenquer.gbk","dabiebandavirus.gbk","ebolavirus.gbk","influenza-a.gbk","hiv.gbk"]

for file in file_names:
    for sq in SeqIO.parse("disease_sequences/"+file,"genbank"):
        AllRecs.append(sq)

AllRecs[0].description="Alenquer virus"
AllRecs[1].description="Severe fever with thrombocytopenia syndrome virus"
AllRecs[2].description="Zaire ebolavirus"
AllRecs[3].description="Influenza A virus"
AllRecs[4].description="Human immunodeficiency virus 1 (HIV-1)"

>>>>>>> 819d0965117b7a8535906257a032041c4ef975df

aligner = Align.PairwiseAligner()
aligner.match_score=1.0


def compare(patientDna,storedData,resultDisease):
    scores=[]
<<<<<<< HEAD
    DiseaseScores={}
=======
>>>>>>> 819d0965117b7a8535906257a032041c4ef975df
    lastm=None
    for rec in storedData:
        result=pairwise2.align.globalxx(patientDna,rec.seq)
        # print(rec.description)
        # print(format_alignment(*result[0], full_sequences=True))
<<<<<<< HEAD
        DiseaseScores[rec.description]=str(aligner.score(patientDna,rec.seq))
=======
>>>>>>> 819d0965117b7a8535906257a032041c4ef975df
        scores.append(aligner.score(patientDna,rec.seq))
        # print(aligner.score(patientDna,rec.seq))
        m=max(scores)
        if(lastm!=m):
            resultDisease=rec.description
        lastm=m
<<<<<<< HEAD
    return{'ResultDisease':resultDisease, 'HighScore':max(scores), 'Allscores':scores,'AllDiseasesScores':DiseaseScores}

# res=None
# a=compare(sseq,AllRecs,res)

# print(a['ResultDisease'])
# print(a['AllDiseasesScores'])


=======
>>>>>>> 819d0965117b7a8535906257a032041c4ef975df


