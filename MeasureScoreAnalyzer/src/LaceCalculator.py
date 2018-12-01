
'''
functions to map dataframe values to LACE scores
'''
def lengthOfStayValueToLScore(n):
    if n<1:
        return 0
    elif n>=1 and n<=4:
        return n
    elif n>4 and n<=6:
        return 4
    elif n>=7 and n<=13:
        return 5
    else:
        return 7


def acuteAdmissionValueToAScore(n):
    if n>0:
        return 3
    else:
        return 0


def comorbidityValueToCScore(n):
    if n < 0:
        #this case shouldn't really be possible
        return 0
    elif n <= 3:
        return n
    else:
        return 5


def edVisitValueToEScore(n):
    if n < 0:
        return 0
    elif n <= 4:
        return n
    else:
        return 4

'''
functions to calculate LACE scores as individual elements
'''
def calculateLScore(measureDF):

    lScore = measureDF.LengthofStay
    lScore = lScore.astype(int)
    lScore = lScore.apply(lengthOfStayValueToLScore)

    return lScore

def calculateAScore(measureDF):

    #missing this data column
    aScore = measureDF.Inpatient_visits
    aScore = aScore.apply(acuteAdmissionValueToAScore)

    return aScore

def calculateCScore(measureDF):

    cScore = measureDF.ComorbidityValue
    cScore = cScore.apply(comorbidityValueToCScore)

    return cScore

def calculateEScore(measureDF):

    eScore = measureDF.ED_visits
    eScore = eScore.astype(int)
    eScore = eScore.apply(edVisitValueToEScore)

    return eScore

'''
function to add L,A,C,E rows to dataframe
'''
def calculateLACEColumns(measureDF):

    lScoreCol = calculateLScore(measureDF)

    aScoreCol = calculateAScore(measureDF)

    cScoreCol = calculateCScore(measureDF)

    eScoreCol = calculateEScore(measureDF)

#     print("{}\n{}\n{}\n{}".format(lScoreCol, aScoreCol, cScoreCol, eScoreCol))
    measureDF = measureDF.assign(LengthOfStayScore=lScoreCol.values)

    measureDF = measureDF.assign(AcuteAdmiisionScore=aScoreCol.values)

    measureDF = measureDF.assign(ComorbidityScore=cScoreCol.values)

    measureDF = measureDF.assign(EDVisitScore=eScoreCol.values)

    return measureDF

'''
function to sum LACE final score
'''
def calculateLACEScore(measureDF):
    columns = ["LengthOfStayScore", "AcuteAdmiisionScore", "ComorbidityScore", "EDVisitScore"]
    laceColumns = measureDF[columns]

    laceScore = laceColumns.sum(axis=1)

    measureDF = measureDF.assign(LACEScore=laceScore.values)
    return measureDF

'''
function to calculate final measure score
measure score = (count LACE score>9)/(count measure rows)
'''
def calculateMeasureScore(measureDF):
    LACEScores=measureDF.LACEScore

    numeratorCol = measureDF[measureDF.LACEScore > 9]
    numerator = float(len(numeratorCol))

    denominator = float(len(measureDF))

    #print("numerator={}, denominator={}".format(numerator, denominator))
    return numerator/denominator