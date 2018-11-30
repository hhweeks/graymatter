from DataReader import readCsvFile, readColumnCSV, buildMeasureDict
from ComorbidityCalculator import getDFRowsForMeasure, getComorbidityCols, getComorbidityValues
from ComorbidityCalculator import addCMValuesToDF
import os

#test
os.chdir("../..")
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

'''
boilerplate setup to test functions
'''
data = readCsvFile("SampleData2016.csv")
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