import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("project110.csv")

temp = df["reading_time"].tolist()

graph = ff.create_distplot( [temp] , ["Reading time Graph"] , show_hist = False)
# graph.show()

mean = statistics.mean(temp)
stdev = statistics.stdev(temp)

print("Mean  : " , mean)
print("Stdev  : " , stdev)

meanList = []

for i in range(1000):
    tempList = []

    for j in range(100):
        tempList.append( random.choice(temp) )

    meanList.append( statistics.mean(tempList) )

meanOfSample = statistics.mean(meanList)
stdevOfSample = statistics.stdev(meanList)

print("Mean of Sample : " , meanOfSample)
print("Stdev of Sample : " , stdevOfSample)

