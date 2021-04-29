
#First we need to read in the dataset to get the information in order to plot the histograms
#We will need pandas to do this.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

filename = 'IrisDataSet.txt'    # df stands for dataframe
df = pd.read_csv(filename)      # this will read the data in as csv format from the txt file and
# we will then base all of our analysis from this table.


setosa=df[df['species']=='setosa']
versicolor=df[df['species']=='versicolor']
virginica=df[df['species']=='virginica']
#print(df.describe)

#print (df.info())

#TypeError: write() argument must be str, not DataFrame. Error recieved before I put str in fromt of df.describe
data = str(df.describe())
set = str(setosa.describe())
ver = str (versicolor.describe())
gin = str(virginica.describe())

print(data)
# check to see if all the species+variables are printed correctly.
#print ("IRIS DATA SET SUMMARY")
#print (data)
#print ("SETOSA DETAILS")
#print(set)
#print ("VERSICOLOR DETAILS")
#print(ver)
#print ("VIRGINICA DETAILS")
#print(gin)

# I want to create a txt file for the summary and write into the file the describe function for both the data and the individual species
file = open("SummaryData.txt","w")
file.write(" IRIS DATA SET SUMMARY \n")
file.write(data)
file.write("\n SETOSA DETAILS \n")
file.write(set)
file.write("\n VERSICOLOR DETAILS \n")
file.write(ver)
file.write("\n VIRGINICA DETAILS \n")
file.write(gin)
file.close()


# https://rpubs.com/shailesh/iris-exploration-correlation

#names of variables
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
#code adapted from https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/
# first type of histogram code is for just the variable and is not species specific.
plt.figure(figsize = (5, 5))
x = df["sepal_length"]
  
plt.hist(x, bins = 10, color = "g")
plt.title("Sepal Length in cm")
plt.xlabel("Sepal_Length_cm")
plt.ylabel("Count")
plt.savefig("Hist Sepal length.png")
plt.show()

plt.figure(figsize = (5, 5))
x = df["sepal_width"]

plt.hist(x, bins = 10, color = "b")
plt.title("Sepal Width in cm")
plt.xlabel("Sepal_Width_cm")
plt.ylabel("Count")
plt.savefig("Hist Sepal Width.png")
plt.show()

plt.figure(figsize = (5, 5))
x = df["petal_length"]

plt.hist(x, bins = 10, color = "m")
plt.title("Petal Length in cm")
plt.xlabel("Petal_Length_cm")
plt.ylabel("Count")
plt.savefig("Hist Petal length.png")
plt.show()


plt.figure(figsize = (5, 5))
x = df["petal_width"]

plt.hist(x, bins = 10, color = "r")
plt.title("Petal Width in cm")
plt.xlabel("Petal_Width_cm")
plt.ylabel("Count")
plt.savefig("Hist Petal Width.png")
plt.show()


# the above code shows the variabes as a whole so I want to see histograms that will differenciate the count according to species.
# code adapted from https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation
plt.figure()

fig,ax=plt.subplots(4,3,figsize=(17, 8))

setosa["sepal_length"].plot(kind="hist", ax=ax[0][0],label="setosa",color ='r',fontsize=10)
versicolor["sepal_length"].plot(kind="hist", ax=ax[0][1],label="versicolor",color='b',fontsize=10)
virginica["sepal_length"].plot( kind="hist",ax=ax[0][2],label="virginica",color='g',fontsize=10)

setosa["sepal_width"].plot(kind="hist", ax=ax[1][0],label="setosa",color ='r',fontsize=10)
versicolor["sepal_width"].plot(kind="hist", ax=ax[1][1],label="versicolor",color='b',fontsize=10)
virginica["sepal_width"].plot( kind="hist",ax=ax[1][2],label="virginica",color='g',fontsize=10)

setosa["petal_length"].plot(kind="hist", ax=ax[2][0],label="setosa",color ='r',fontsize=10)
versicolor["petal_length"].plot(kind="hist", ax=ax[2][1],label="versicolor",color='b',fontsize=10)
virginica["petal_length"].plot( kind="hist",ax=ax[2][2],label="virginica",color='g',fontsize=10)


setosa["petal_width"].plot(kind="hist", ax=ax[3][0],label="setosa",color ='r',fontsize=10)
versicolor["petal_width"].plot(kind="hist", ax=ax[3][1],label="versicolor",color='b',fontsize=10)
virginica["petal_width"].plot( kind="hist",ax=ax[3][2],label="virginica",color='g',fontsize=10)

plt.rcParams.update({'font.size': 10})
plt.tight_layout()

ax[0][0].set(title='SepalLengthCm')
ax[0][1].set(title='SepalLengthCm')
ax[0][2].set(title='SepalLengthCm')
ax[1][0].set(title='SepalWidthCm ')
ax[1][1].set(title='SepalWidthCm ')
ax[1][2].set(title='SepalWidthCm ')
ax[2][0].set(title='PetalLengthCm')
ax[2][1].set(title='PetalLengthCm ')
ax[2][2].set(title='PetalLengthCm')
ax[3][0].set(title='PetalWidthCm')
ax[3][1].set(title='PetalWidthCm')
ax[3][2].set(title='PetalWidthCm')

ax[0][0].legend()
ax[0][1].legend()
ax[0][2].legend()
ax[1][0].legend()
ax[1][1].legend()
ax[1][2].legend()
ax[2][0].legend()
ax[2][1].legend()
ax[2][2].legend()
ax[3][0].legend()
ax[3][1].legend()
ax[3][2].legend()


plt.show()
plt.close()

#https://seaborn.pydata.org/tutorial/distributions.html
# https://towardsdatascience.com/how-to-use-seaborn-for-data-visualization-4c61fc488ec1
#https://seaborn.pydata.org/generated/seaborn.kdeplot.html
#https://web.microsoftstream.com/video/f8fbdd37-3586-4f0d-82c4-7bda05470ff4

# Although the species specific histograms are more useful to visualize the data it would be better to superimpose these
# counts per species on one histogram plt per variable as below with the displot and the kde .I changed different 
# components like the colour and bin number and I kept the kde=True for the graph.
# FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function 
# with similar flexibility) or `histplot` (an axes-level function for histograms). I did update the code to change the displot with
# histplot and displot. But the putput was not as aesthetically pleasing I kept the code as distplot.


plt.figure()
sns.distplot(setosa["sepal_length"])
sns.distplot(setosa["sepal_length"],bins=25, kde=True, color='fuchsia', label='Setosa')
sns.distplot(versicolor["sepal_length"])
sns.distplot(versicolor["sepal_length"],bins=25, kde=True,color= 'b', label='Versicolor')
sns.distplot(virginica["sepal_length"])
sns.distplot(virginica["sepal_length"],bins=25, kde=True,color= 'aqua', label='Virginica')
plt.legend()
plt.title("Sepal Length for different Species")
plt.xlabel("Sepal Length in cm")
plt.ylabel("Distribution of Sepal length")

plt.show()

plt.figure()
sns.distplot(setosa["sepal_width"])
sns.distplot(setosa["sepal_width"],bins=25, kde=True, color='fuchsia', label='Setosa')
sns.distplot(versicolor["sepal_width"])
sns.distplot(versicolor["sepal_width"],bins=25, kde=True,color= 'b', label='Versicolor')
sns.distplot(virginica["sepal_width"])
sns.distplot(virginica["sepal_width"],bins=25, kde=True,color= 'aqua', label='Virginica')
plt.legend()
plt.title("Sepal Width Cm for different Species")
plt.xlabel("Sepal Width in cm")
plt.ylabel("Distribution of Sepal Width")

plt.show()


plt.figure()
sns.distplot(setosa["petal_length"])
sns.distplot(setosa["petal_length"],bins=25, kde=True, color='fuchsia', label='Setosa')
sns.distplot(versicolor["petal_length"])
sns.distplot(versicolor["petal_length"],bins=25, kde=True,color= 'b', label='Versicolor')
sns.distplot(virginica["petal_length"])
sns.distplot(virginica["petal_length"],bins=25, kde=True,color= 'aqua', label='Virginica')
plt.legend()
plt.title("Petal Length for different Species")
plt.xlabel("Petal Length in cm")
plt.ylabel("Distribution of Petal length")

plt.show()

plt.figure()
sns.distplot(setosa["petal_width"])
sns.distplot(setosa["petal_width"],bins=25, kde=True, color='g', label='Setosa')
sns.distplot(versicolor["petal_width"])
sns.distplot(versicolor["petal_width"],bins=25, kde=True,color= 'b', label='Versicolor')
sns.distplot(virginica["petal_width"])
sns.distplot(virginica["petal_width"],bins=25, kde=True,color= 'r', label='Virginica')
plt.legend()
plt.title("Petal Width for different Species")
plt.xlabel("Petal Width in cm")
plt.ylabel("Distribution of Petal Width")

plt.show()
plt.close()

#https://seaborn.pydata.org/generated/seaborn.kdeplot.html
#https://web.microsoftstream.com/video/f8fbdd37-3586-4f0d-82c4-7bda05470ff4

# Next code was written for scatterplots of the dataset

# This scatterplot is not species specific so does not render much information other than the distribution
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
plt.close

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
# https://rpubs.com/shailesh/iris-exploration-correlation

plt.figure(figsize=(7,4)) 
sns.heatmap(df.corr(),annot=True)
plt.show()


#Above is code for a heatmap from the seaborn library. Heat maps display numeric tabular data 
# where the cells are colored depending upon the contained value. Heat maps are great 
# for making trends in # this kind of data more readily apparent, particularly when the data
# is ordered and there is clustering or in this case correlation.

#https://www.datacamp.com/community/tutorials/introduction-machine-learning-python?utm_source=adwords_ppc&utm_campaignid=898687156&utm_adgroupid=48947256715&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=229765585186&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=20487&gclid=Cj0KCQjw9_mDBhCGARIsAN3PaFMqV46OWTzY86tg_8vc0yBOr_Z2-IGgk8fhj_zxq5z-agq1-nRwRbYaAtOeEALw_wcB


#sns.scatterplot(x='sepal_length', y='sepal_width', data=df, hue='species')
#plt.title("Sepal Length vs Sepal Width") 
#plt.xlabel("Sepal Length") 
#plt.ylabel("Sepal Width")



#Multivariate Analysis:
sns.pairplot (df, hue = 'species')

plt.show()

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

