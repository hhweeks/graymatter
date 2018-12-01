import os

from src.MeasureScoreCalculator import *

os.chdir("../data/")
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
measureName = "COPD"
diagnsosisCodeDir = "DiagnosisCode/"
comorbidityColumnsDir = "ComorbidityColumns/"
measureScore = getMeasureScore(measureName,diagnsosisCodeDir,comorbidityColumnsDir)
print(measureScore)