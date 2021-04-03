import sys
# print('Python: {}'.format(sys.version))-check what version python 3.8.5 installed

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
import seaborn as sns

def header (msg):
    header('Read Iris Data into a df')
filename = 'IrisDataSet.txt' # df stands for dataframe
df = pd.read_csv(filename) # this will read the data in as csv format from the txt file and we will then base all of our analysis from this table

#print(df)-check and see if the data has read into this file correctly

#print (df['species'].unique())- this will print out an array of the unique species types

# now we will create a a dataframe for each species using boolean notation for this . When I originally did this I got a NaN in the output because I did not print the species names correctly.
# I used Iris-setosa instead of jsut setosa. Naming must be exact in all code !!! I removed the Iris and renamed the species correctly to reflect what was in the df

setosa=df[df['species']=='setosa']
versicolor=df[df['species']=='versicolor']
virginica=df[df['species']=='virginica']

#print(setosa.describe())
#print(versicolor.describe())
#print(virginica.describe())

# now we can describe the datafile using describe () which we returen the count,mean,SD,CV,percentiles,min and max of all the 4 variables (length+width of petal and length+width of sepal)
#df.describe()

##Plotting Petal Length vs Petal Width & Sepal Length vs Sepal width 
plt.figure()
fig,ax=plt.subplots(1,2,figsize=(5, 5))
df.plot(x="sepal_length",y="sepal_width",kind="scatter",ax=ax[0],sharex=False,sharey=False,label="sepal",color='r')
df.plot(x="petal_length",y="petal_width",kind="scatter",ax=ax[1],sharex=False,sharey=False,label="petal",color='b')
ax[0].set(title='Sepal comparasion ', ylabel='sepal-width')
ax[1].set(title='Petal Comparasion',  ylabel='petal-width')
ax[0].legend()
ax[1].legend()

#plt.show()
#plt.close

# https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation

plt.figure()
fig,ax=plt.subplots(1,2,figsize=(10, 5))

setosa.plot(x="sepal_length", y="sepal_width", kind="scatter",ax=ax[0],label='setosa',color='r')
versicolor.plot(x="sepal_length",y="sepal_width",kind="scatter",ax=ax[0],label='versicolor',color='b')
virginica.plot(x="sepal_length", y="sepal_width", kind="scatter", ax=ax[0], label='virginica', color='g')

setosa.plot(x="petal_length", y="petal_width", kind="scatter",ax=ax[1],label='setosa',color='r')
versicolor.plot(x="petal_length",y="petal_width",kind="scatter",ax=ax[1],label='versicolor',color='b')
virginica.plot(x="petal_length", y="petal_width", kind="scatter", ax=ax[1], label='virginica', color='g')

ax[0].set(title='Sepal comparasion ', ylabel='sepal-width')
ax[1].set(title='Petal Comparasion',  ylabel='petal-width')
ax[0].legend()
ax[1].legend()
plt.show()

# looking at the plot from the above code Iris Setosa is easily distinguishable from the oher two species. Iris versicolor and virginica are quite comparable in these plots and would 
# not be easily identified graphically here.

