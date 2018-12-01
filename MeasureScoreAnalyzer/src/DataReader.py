import pandas as pd
from os import walk
from os import chdir

'''
function to read raw data from
takes arg of csv filename
drops incomplete rows (with NaN)
return data as pandas dataframe
'''
def readDataCsv(filename):
    data = pd.read_csv(filename)
    data = data.dropna()#
    return data

'''
function to read csv of 1 column, return as pair : column label, [column values]
used to read diagnosis codes AND comorbidity column names
takes arg of csv filename
returns pair (key measure, value [list diagnosis codes])
'''
def readColumnCSV(filename):
    measureData = pd.read_csv(filename, dtype={0: str})#want dc as string even if it appears numerical

    measureDataColumns = measureData.columns.values.tolist()

    #assert that the list is length 1
    if len(measureDataColumns) > 1:
        raise ValueError("Diagnosis Code file {} contained too many columns, expected 1 column found {}"
                         .format(filename, len(measureDataColumns)))

    measure = measureDataColumns[0]
    diagnosisCodes = measureData[measure].values.tolist()

    return (measure, diagnosisCodes)

'''
function to build a mapping from a measure to metadata (i.e. diagnosis codes, comorbidity column names)
takes arg dir name where csv's are located
returns dictionary
'''
def buildMeasureDict(directory):

    measureDict = {}
    fileList = []

    #get filenames
    for (dirpath, dirname, filenames) in walk(directory):
        fileList.extend(filenames)
        break

    #cd to appropraite directory
    chdir(directory)

    for filename in fileList:
        (measure, diagnosisCodes) = readColumnCSV(filename)
        measureDict[measure] = diagnosisCodes

    chdir("..")

    return measureDict

