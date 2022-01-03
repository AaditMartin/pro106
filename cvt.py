import csv
import numpy as np 
import plotly.express as px

def plotGraph(data_path):
    with open(data_path) as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df,x='Temperature',y='Ice-cream Sales')
        fig.show()
    
def getDataSource(data_path):
    ics=[]
    cds=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            ics.append(float(row['Temperature']))
            cds.append(float(row['Ice-cream Sales']))
    return{'x':ics,'y':cds}

def find_correlation(data_src):
    correlation=np.corrcoef(data_src['x'],data_src['y'])
    print('correlation between temperature vs ice cream sales: ',correlation[0,1])

def setup():
    data_path='dataset1.csv'
    data_src=getDataSource(data_path)
    find_correlation(data_src)
    plotGraph(data_path)

setup()            