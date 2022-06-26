import plotly.express as px
import csv
import numpy as np

def getDataSource(dataPath):
    iceCreamSales = []
    coldDrinkSales = []
    
    with open(dataPath) as f:
        csv_reader = csv.DictReader(f)
        for i in csv_reader:
            iceCreamSales.append(float(i["Marks In Percentage"]))
            coldDrinkSales.append(float(i["Days Present"]))

    return{"x":iceCreamSales, "y": coldDrinkSales}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation Student Marks and Days Present is: ", correlation[0,1])

def setup():
    dataPath = "Student Marks vs Days Present.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)

setup()