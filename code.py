import plotly.figure_factory as ff
import statistics
import pandas as pd
import random

df=pd.read_csv("medium_data.csv")
data=df['claps'].tolist()

mean=statistics.mean(data)
std=statistics.stdev(data)

print ("mean = " , mean)
print ("std = " , std)
print ( len(data))

def generateSample(numberofsamples):
    sample=[]
    for i in range(numberofsamples):
        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        sample.append(value)

    sampleMean=statistics.mean(sample)
    return sampleMean

def showfig(mean_list):
    fig=ff.create_distplot([mean_list] , ["claps"] , show_hist=False)
    fig.show()

def setup():
    mean_list=[]

    for i in range(0,100):
        sampleMean=generateSample(30)
        mean_list.append(sampleMean)

    mean=statistics.mean(mean_list)    
    std=statistics.stdev(mean_list)
    print("STD of Sample means = " ,std)
    print("Mean of Sample means =" , mean)
    showfig(mean_list)        

setup()    