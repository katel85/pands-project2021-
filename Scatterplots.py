# https://www.educba.com/scatterplots-in-r/
# Descriptive statistics and plots with pandas https://web.microsoftstream.com/video/ecc9ce4a-c6f5-4c50-a4f4-29116fc21b81
# https://pythonbasics.org/seaborn-pairplot/#:~:text=The%20pairplot%20function%20creates%20a,axis%20across%20a%20single%20column.



import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

filename = 'IrisDataSet.txt' # df stands for dataframe
df = pd.read_csv(filename) 

#names of variables
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

#data frame code for seperating each species from https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation
#seperating them by species
setosa=df[df['species']=='setosa']
versicolor=df[df['species']=='versicolor']
virginica=df[df['species']=='virginica']


# code for scatterplot of each pair of variables below. This scatterplot is not 
# species specific so does not render much information other than the distribution
# overall of the paired variables.

plt.figure()
fig,ax=plt.subplots(1,2,figsize=(5, 5))
df.plot(x="sepal_length",y="sepal_width",kind="scatter",ax=ax[0],sharex=False,sharey=False,label="sepal",color='r')
df.plot(x="petal_length",y="petal_width",kind="scatter",ax=ax[1],sharex=False,sharey=False,label="petal",color='b')
ax[0].set(title='Sepal comparasion ', ylabel='sepal-width')
ax[1].set(title='Petal Comparasion',  ylabel='petal-width')
ax[0].legend()
ax[1].legend()

plt.show()
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

#sns.scatterplot(x='sepal_length', y='sepal_width', data=df, hue='species')
#plt.title("Sepal Length vs Sepal Width") 
#plt.xlabel("Sepal Length") 
#plt.ylabel("Sepal Width")



#Multivariate Analysis:
sns.pairplot (df, hue = 'species')

plt.show()

