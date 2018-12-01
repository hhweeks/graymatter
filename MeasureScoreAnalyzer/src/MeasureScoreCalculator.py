from src.ComorbidityCalculator import getComorbidityCols, getDFRowsForMeasure, getComorbidityValues, addCMValuesToDF
from src.LaceCalculator import calculateLACEColumns, calculateLACEScore, calculateMeasureScore

from src.DataReader import readDataCsv, buildMeasureDict


def getMeasureScore(measureName, dataFile, diagnosisCodeDir, comorbidityColumnsDir):

    if(dataFile):
        data = readDataCsv(dataFile)
    else:
        data = readDataCsv("SampleData2016.csv")

    measureDict = buildMeasureDict(diagnosisCodeDir)
    comorbidityDict = buildMeasureDict(comorbidityColumnsDir)

    measureDF = getDFRowsForMeasure(data, measureDict, measureName)
    submeasureDF = getComorbidityCols(measureDF, comorbidityDict, measureName)
    comorbidityValues = getComorbidityValues(submeasureDF)
    measureDF = addCMValuesToDF(measureDF, comorbidityValues)

    measureDF = calculateLACEColumns(measureDF)
    measureDF = calculateLACEScore(measureDF)

    measureScore = calculateMeasureScore(measureDF)

    return measureScore