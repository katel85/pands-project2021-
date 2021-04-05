#  Adapted from Exploratory Data Analysis of IRIS Data Set Using Python
# Author Catherine Leddy
# Ref https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
col=['sepal_length','sepal_width','petal_length','petal_width','type']
iris=pd.read_csv("IrisDataSet2.txt",names=col)

#print(iris)-check that dataset has been read in

#print("First five rows")
#print(iris.head())
#print("*********")
#print("columns",iris.columns)
#print("*********")
#print("shape:",iris.shape)
#print("*********")
#print("Size:",iris.size)
#print("*********")
#print("no of samples available for each type") 
#print(iris["type"].value_counts())
#print("*********")
#print(iris.describe())

# below code will detail the flowers separately
iris_setosa=iris.loc[iris["type"]=="Iris-setosa"]
iris_virginica=iris.loc[iris["type"]=="Iris-virginica"]
iris_versicolor=iris.loc[iris["type"]=="Iris-versicolor"]

# When below code was executed my terminla read an error message but still displayed the plot.
# Error message FutureWarning: `distplot` is a deprecated function and will be removed in a future version. 
# Please adapt your code to use either `displot` (a figure-level function  with similar flexibility) or `histplot` (an axes-level function for histograms). 
# I then replaced distplot with displot in the code.

#sns.FacetGrid(iris,hue="type",height=3).map(sns.distplot,"petal_length").add_legend()
#sns.FacetGrid(iris,hue="type",height=3).map(sns.distplot,"petal_width").add_legend()
#sns.FacetGrid(iris,hue="type",height=3).map(sns.distplot,"sepal_length").add_legend()
#sns.FacetGrid(iris,hue="type",height=3).map(sns.distplot,"sepal_width").add_legend()
#plt.show()


#sns.FacetGrid(iris,hue="type",height=3).map(sns.histplot,"petal_length").add_legend()
#sns.FacetGrid(iris,hue="type",height=3).map(sns.histplot,"petal_width").add_legend()
#sns.FacetGrid(iris,hue="type",height=3).map(sns.histplot,"sepal_length").add_legend()
#sns.FacetGrid(iris,hue="type",height=3).map(sns.histplot,"sepal_width").add_legend()
#plt.show()

sns.boxplot(x="type",y="petal_length",data=iris)
plt.show()
