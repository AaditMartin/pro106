import csv
import numpy as np 
import plotly.express as px

def plotGraph(data_path):
    with open(data_path) as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.bar(df,x='Size of TV',y='Average time spent')
        fig.show()
    
def getDataSource(data_path):
    ics=[]
    cds=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            ics.append(float(row['Size of TV']))
            cds.append(float(row['Average time spent']))
    return{'x':ics,'y':cds}

def find_correlation(data_src):
    correlation=np.corrcoef(data_src['x'],data_src['y'])
    print('correlation between Size of TV vs Average time spent: ',correlation[0,1])

def setup():
    data_path='dataset2.csv'
    data_src=getDataSource(data_path)
    find_correlation(data_src)
    plotGraph(data_path)

setup()            