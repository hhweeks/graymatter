import os

from src.DataReader import readDataCsv, readColumnCSV, buildMeasureDict

#test functions
os.chdir("../data/")
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

data = readDataCsv("SampleData2016.csv")

#read diagnosis codes from csv, build map
pair = readColumnCSV("DiagnosisCode/AMI.csv")
measureDict = buildMeasureDict("DiagnosisCode/")

#read comorbidity columns labels from csv, build
amiCM = readColumnCSV("ComorbidityColumns/AMI.csv")
comorbidityDict = buildMeasureDict("ComorbidityColumns/")