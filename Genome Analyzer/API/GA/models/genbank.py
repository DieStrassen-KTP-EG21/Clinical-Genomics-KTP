from re import fullmatch
from Bio import SeqIO,pairwise2,Align
from Bio.pairwise2 import format_alignment
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

AllRecs=[]
file_names=["alenquer.gbk","dabiebandavirus.gbk","ebolavirus.gbk","influenza-a.gbk","hiv.gbk","sars.gbk"]

for file in file_names:
    for sq in SeqIO.parse("GA/models/disease_sequences/"+file,"genbank"):
        AllRecs.append(sq)

# sseq=Seq("CGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTACGTAGCTAGTGCTAGTCGTAGCAGTCGTGTCAGTCGTACGTATGCTGATGCTAGCGTA")

aligner = Align.PairwiseAligner()
aligner.match_score=1.0


def compare(patientDna,storedData,resultDisease):
    scores=[]
    DiseaseScores={}
    lastm=None
    for rec in storedData:
        result=pairwise2.align.globalxx(patientDna,rec.seq)
        # print(rec.description)
        # print(format_alignment(*result[0], full_sequences=True))
        DiseaseScores[rec.description]=str(aligner.score(patientDna,rec.seq))
        scores.append(aligner.score(patientDna,rec.seq))
        # print(aligner.score(patientDna,rec.seq))
        m=max(scores)
        if(lastm!=m):
            resultDisease=rec.description
        lastm=m
    return{'ResultDisease':resultDisease, 'HighScore':max(scores), 'Allscores':scores,'AllDiseasesScores':DiseaseScores}

# res=None
# a=compare(sseq,AllRecs,res)

# print(a['ResultDisease'])
# print(a['AllDiseasesScores'])




