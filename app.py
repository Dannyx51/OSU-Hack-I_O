import numpy as np
from random import uniform
import pandas as pd
import matplotlib.pyplot as plt
import xlrd 

data = [[] for x in range(250)]

# General randomized data
for y in range(250):  
    data[y].append(uniform(-81.315,-86.457))
    data[y].append(uniform(40.371, 37.523))

#Cincinnati
dCincy = [[] for x in range(50)]
for y in range(50):
    dCincy[y].append(uniform(-82.9329,-83.5377))
    dCincy[y].append(uniform(38.5448,38.9263))
data.extend(dCincy)

#Mason
dMason = [[] for x  in range(25)]
for y in range(25):
    dMason[y].append(uniform(-83.2171, -83.5537))
    dMason[y].append(uniform(38.4062, 38.6911))
data.extend(dMason)

#:bus
dBus = [[] for x in range(75)]
for y in range(75):
    dBus[y].append(uniform(-84.495, -84.9725))
    dBus[y].append(uniform(37.732, 38.0306))
data.extend(dBus)

df = pd.DataFrame(data, columns= ['longitude','latitude'])

df.head()

BBox = ((-81.315, -86.457, 40.371, 37.523))

ruh_m = plt.imread('map.png')

fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(df.longitude, df.latitude, zorder=1, alpha= 0.2, c='b', s=10)
ax.set_title('Plotting Positivity in Ohio')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
ax.imshow(ruh_m, zorder=0, extent = BBox, aspect = 'equal')

plt.show()