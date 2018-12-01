import os
import sys

from src.MeasureScoreCalculator import getMeasureScore

from src.DataReader import readColumnCSV


def printUsage():
    print("incorrect usage\nplease use python3 Main.py MEASURE_NAME (optional)DATAFILE.csv")
    print("if specified, DATAFILE should be located in data/ directory")
    print("valid MEASURE_NAME :")
    (mn ,validMeasureNames) = readColumnCSV("MeasureNames/MeasureNames.csv")
    for measureName in validMeasureNames:
        print("\t{}".format(measureName))

def getMeasureFromArg(arg1):
    (mn ,validMeasureNames) = readColumnCSV("MeasureNames/MeasureNames.csv")
    arg1 = arg1.upper()
    if arg1 in validMeasureNames:
        return arg1
    else:
        printUsage()
        return None

#run script
dataFile = None
diagnsosisCodeDir = "DiagnosisCode/"
comorbidityColumnsDir = "ComorbidityColumns/"

os.chdir("data/")
dir_path = os.path.dirname(os.path.realpath(__file__))

measureName = None
measureScore = None

#arg0 py file, arg1 measure name
if(len(sys.argv)<2):
    printUsage()
else:
    measureName = getMeasureFromArg(sys.argv[1])

#arg2 datafile.csv
if(len(sys.argv)==3):
    dataFile = sys.argv[2]

if measureName:
    measureScore = getMeasureScore(measureName, dataFile, diagnsosisCodeDir, comorbidityColumnsDir)
    print("{} Measure Score:".format(measureName))
    print(measureScore)