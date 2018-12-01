import os

from src.ComorbidityCalculator import *
from src.LaceCalculator import *

from src.DataReader import *

#test
os.chdir("../data/")
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)


l1 = []
for n in range(-1,17):
    l1.append((n,lengthOfStayValueToLScore(n)))
print(l1)

l2=[]
for valuestr in range(-1,3):
    l2.append((valuestr,acuteAdmissionValueToAScore(valuestr)))
print(l2)

l3=[]
for n in range(-1,7):
    l3.append((n, comorbidityValueToCScore(n)))
print(l3)

l4=[]
for n in range(-1, 6):
    l4.append((n, edVisitValueToEScore(n)))
print(l4)

'''
boilerplate setup to test functions
'''
data = readDataCsv("SampleData2016.csv")
measureDict = buildMeasureDict("DiagnosisCode/")

amiDF = getDFRowsForMeasure(data, measureDict, "AMI")
comorbidityDict = buildMeasureDict("ComorbidityColumns/")

submeasureDF = getComorbidityCols(amiDF, comorbidityDict, "AMI")
comorbidityValuesAMI = getComorbidityValues(submeasureDF)
amiDF = addCMValuesToDF(amiDF, comorbidityValuesAMI)
'''
'''

calculateLScore(amiDF)
calculateAScore(amiDF)
calculateCScore(amiDF)
calculateEScore(amiDF)

amiDF = calculateLACEColumns(amiDF)
# print(amiDF)

amiDF = calculateLACEScore(amiDF)
print(amiDF)

finalScore = calculateMeasureScore(amiDF)
print(finalScore)