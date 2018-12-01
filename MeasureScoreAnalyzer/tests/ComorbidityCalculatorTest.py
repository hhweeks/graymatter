import os

from src.ComorbidityCalculator import addCMValuesToDF
from src.ComorbidityCalculator import getDFRowsForMeasure, getComorbidityCols, getComorbidityValues

from src.DataReader import readDataCsv, readColumnCSV, buildMeasureDict

#test
os.chdir("../data/")
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

'''
boilerplate setup to test functions
'''
data = readDataCsv("SampleData2016.csv")
pair = readColumnCSV("DiagnosisCode/AMI.csv")
measureDict = buildMeasureDict("DiagnosisCode/")
'''
'''

amiDF = getDFRowsForMeasure(data, measureDict, "AMI")
# print(amiDF)

comorbidityDict = buildMeasureDict("ComorbidityColumns/")
submeasureDF = getComorbidityCols(amiDF, comorbidityDict, "AMI")
# print(submeasureDF)

comorbidityValuesAMI = getComorbidityValues(submeasureDF)
# print(comorbidityValuesAMI)

amiDF = addCMValuesToDF(amiDF, comorbidityValuesAMI)
print(amiDF)