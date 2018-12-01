from ComorbidityCalculator import getComorbidityCols, getDFRowsForMeasure, getComorbidityValues, addCMValuesToDF
from DataReader import readCsvFile, buildMeasureDict
from LaceCalculator import calculateLACEColumns, calculateLACEScore, calculateMeasureScore


def getMeasureScore(measureName, diagnosisCodeDir, comorbidityColumnsDir):

    data = readCsvFile("SampleData2016.csv")
    measureDict = buildMeasureDict(diagnosisCodeDir)
    comorbidityDict = buildMeasureDict(comorbidityColumnsDir)

    measureDF = getDFRowsForMeasure(data, measureDict, measureName)
    submeasureDF = getComorbidityCols(measureDF, comorbidityDict, "AMI")
    comorbidityValues = getComorbidityValues(submeasureDF)
    measureDF = addCMValuesToDF(measureDF, comorbidityValues)

    measureDF = calculateLACEColumns(measureDF)
    measureDF = calculateLACEScore(measureDF)

    measureScore = calculateMeasureScore(measureDF)

    return measureScore

import os
os.chdir("..")
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
measureName = "COPD"
diagnsosisCodeDir = "DiagnosisCode/"
comorbidityColumnsDir = "ComorbidityColumns/"
print(getMeasureScore(measureName,diagnsosisCodeDir,comorbidityColumnsDir))