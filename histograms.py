# Part of the project is to create histograms for each of the variables in the Iris Dataset 
# Below we will work with code to display the histograms of each of the varibles.
# The variables in the dataset are sepal width, sepal length, petal width and petal length.
# Species is also a variable in this dataset so we will create a histogram for this although it will be quite boring to look at!
# This means we are going to create 5 histograms for the above variables.


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

#names of variables
#names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
#code adapted from https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/
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


#plt.figure(figsize = (5, 5))
#x = df["species"]

#plt.hist(x, bins = 5, color = "c")
#plt.title("species")
#plt.xlabel("species")
#plt.ylabel("Count")
#plt.show()

# the above code shows the variabes as a whole so I want to see histograms that will diffrenciate the count according to species.
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

# Although the species specific histograms are more useful to visualize the data it would be better to superimpose these
# counts per species on one histogram plt per variable as below with the displot and the kde .I changed different 
# components like the colour and bin number but found the kde component the best to distinguish the species.
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


#https://seaborn.pydata.org/tutorial/distributions.html
# https://towardsdatascience.com/how-to-use-seaborn-for-data-visualization-4c61fc488ec1
#https://seaborn.pydata.org/generated/seaborn.kdeplot.html
#https://web.microsoftstream.com/video/f8fbdd37-3586-4f0d-82c4-7bda05470ff4
#code adapted from https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/


