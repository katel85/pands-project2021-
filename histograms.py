# Part of the project is to create histograms for each of the variables in the Iris Dataset 
# Below we will work with code to display the histograms of each of the varibles.
# The variables in the dataset are sepal widrth, sepal length, petal width and petal length.
# This means we are going to create 4 histograms for the above variables.

#https://web.microsoftstream.com/video/f8fbdd37-3586-4f0d-82c4-7bda05470ff4

#First we need to read in the dataset to get the information in order to plot the histograms
#We will need pandas to do this.

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
import seaborn as sns

filename = 'IrisDataSet.txt' # df stands for dataframe
df = pd.read_csv(filename) # this will read the data in as csv format from the txt file and
# we will then base all of our analysis from this table.

#print(df.describe)

#print (df.info())

#names of variables
#names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

plt.figure(figsize = (10, 7))
x = df["sepal_length"]
  
plt.hist(x, bins = 20, color = "g")
plt.title("Sepal Length in cm")
plt.xlabel("Sepal_Length_cm")
plt.ylabel("Count")
plt.show()

plt.figure(figsize = (10, 7))
x = df["sepal_width"]

plt.hist(x, bins = 20, color = "b")
plt.title("Sepal Width in cm")
plt.xlabel("Sepal_Width_cm")
plt.ylabel("Count")
plt.show()

plt.figure(figsize = (10, 7))
x = df["petal_length"]

plt.hist(x, bins = 20, color = "m")
plt.title("Petal Length in cm")
plt.xlabel("Petal_Length_cm")
plt.ylabel("Count")
plt.show()


plt.figure(figsize = (10, 7))
x = df["petal_width"]

plt.hist(x, bins = 20, color = "r")
plt.title("Petal Width in cm")
plt.xlabel("Petal_Width_cm")
plt.ylabel("Count")
plt.show()


plt.figure(figsize = (10, 7))
x = df["species"]

plt.hist(x, bins = 20, color = "c")
plt.title("species")
plt.xlabel("species")
plt.ylabel("Count")
plt.show()




