import plotly.express as px
import csv
import numpy as np

def getDataSource(dataPath):
    iceCreamSales = []
    coldDrinkSales = []
    
    with open(dataPath) as f:
        csv_reader = csv.DictReader(f)
        for i in csv_reader:
            iceCreamSales.append(float(i["Coffee in ml"]))
            coldDrinkSales.append(float(i["sleep in hours"]))

    return{"x":iceCreamSales, "y": coldDrinkSales}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between coffee in ml and sleep in hours is: ", correlation[0,1])

def setup():
    dataPath = "cups of coffee vs hours of sleep.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)

setup()