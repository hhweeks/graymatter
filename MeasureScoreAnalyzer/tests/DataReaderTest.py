from DataReader import readCsvFile, readColumnCSV, buildMeasureDict
import os

#test functions
os.chdir("../..")
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

data = readCsvFile("SampleData2016.csv")

#read diagnosis codes from csv, build map
pair = readColumnCSV("DiagnosisCode/AMI.csv")
measureDict = buildMeasureDict("DiagnosisCode/")

#read comorbidity columns labels from csv, build
amiCM = readColumnCSV("ComorbidityColumns/AMI.csv")
comorbidityDict = buildMeasureDict("ComorbidityColumns/")