from src.DataReader import readColumnCSV
import os

os.chdir("../data/")
(mn, measureNames) = readColumnCSV("MeasureNames/MeasureNames.csv")
os.chdir("..")
for name in measureNames:
    pass
    os.system('python3 Main.py {}'.format(name))