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
#plt.show()

# Correlation between variables
print(df.corr(method='pearson'))

plt.figure(figsize=(7,4)) 
sns.heatmap(df.corr(),annot=True)
plt.show()

#Above is code for a heatmap from the seaborn library. Heat maps display numeric tabular data 
# where the cells are colored depending upon the contained value. Heat maps are great 
# for making trends in # this kind of data more readily apparent, particularly when the data
# is ordered and there is clustering or in this case correlated.

#https://www.datacamp.com/community/tutorials/introduction-machine-learning-python?utm_source=adwords_ppc&utm_campaignid=898687156&utm_adgroupid=48947256715&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=229765585186&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=20487&gclid=Cj0KCQjw9_mDBhCGARIsAN3PaFMqV46OWTzY86tg_8vc0yBOr_Z2-IGgk8fhj_zxq5z-agq1-nRwRbYaAtOeEALw_wcB


#sns.scatterplot(x='sepal_length', y='sepal_width', data=df, hue='species')
#plt.title("Sepal Length vs Sepal Width") 
#plt.xlabel("Sepal Length") 
#plt.ylabel("Sepal Width")



#Multivariate Analysis:
#sns.pairplot (df, hue = 'species')

#plt.show()

#sns.set(style='whitegrid')
#sns.swarmplot(x="species", y="petal_length", data=df)
#plt.show()


#fig=plt.gcf()
#fig.set_size_inches(10,7)
#fig=sns.stripplot(x='species',y='sepal_length',data=df,jitter=True,edgecolor='gray',size=8,palette='winter',orient='v')
#plt.show()

#plt.figure()
#sns.stripplot(x='species',y='petal_length',data=df,jitter=True,edgecolor='gray',size=8,palette='winter',orient='v')
#plt.show()

# https://medium.com/@neuralnets/data-visualization-with-python-and-seaborn-part-1-29c9478a8700


#sns.stripplot(x='Species',y='SepalLengthCm',data=iris,jitter=True,edgecolor='gray')
#plt.figure(figsize = (10, 10))
#sns.lmplot(x="petal_length", y="sepal_length",data=df)
#sns.lmplot(x="petal_length", y="sepal_width", data=df)
#plt.show()
# Although the code above shows the linear regression and the scatter. I didn't like particularly the format
# of the plot when it was generated so I tried again with code for the regplot. 
# code adapted from https://seaborn.pydata.org/tutorial/regression.html
plt.figure()
sns.regplot(x=df["petal_length"], y=df["petal_width"], line_kws={"color":"r","alpha":0.7,"lw":5})
plt.show()

plt.figure()
sns.regplot(x=df["petal_length"], y=df["sepal_width"], line_kws={"color":"r","alpha":0.7,"lw":5})
plt.show()
# code adapted from https://www.python-graph-gallery.com/42-custom-linear-regression-fit-seaborn


