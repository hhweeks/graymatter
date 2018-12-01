import pandas as pd
'''
function that returns a dataframe of the rows with the diagnosis codes corresponding to each measure
'''
def getDFRowsForMeasure(dataframe, measureDict, measure):
    diagnosisCodeList = measureDict[measure]
    subdataframe = dataframe[dataframe.diagnosis_code.isin(diagnosisCodeList)]

    return subdataframe
'''
function to return dataframe cols assoc with measure
given: measure dictionary, comorbidity dictionary, measure dataframe (df with rows belonging to 1 measure)
'''
def getComorbidityCols(measureDF, comorbidityDict, measure):
    cmList = comorbidityDict[measure]

    #drop measureDF cols not in cmList
    submeasureDF = measureDF[cmList]

    return submeasureDF

'''
function to calculate comorbidity values
'''
def getComorbidityValues(submeasureDF):

    #count occurences of values per row (i.e. yes=f1, no=f2)
    valueCount = submeasureDF.apply(pd.Series.value_counts, axis=1)

    #replace nan values with 0 (nan prevents transform to int)
    valueCount = valueCount.fillna(0)

    #transform float to int
    valueCount = valueCount.astype(int)

    return valueCount["Yes"]

'''
add comorbidity value back on to measureDF
'''
def addCMValuesToDF(measureDF, comorbidityValuesDF):
    measureDF = measureDF.assign(ComorbidityValue=comorbidityValuesDF.values)

    return measureDF


