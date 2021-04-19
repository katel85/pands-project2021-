# Create summary txt output files for each of the variables in the Fisher Iris Data Set
# Author Catherine Leddy

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
import seaborn as sns

filename = 'IrisDataSet.txt' # df stands for dataframe
df = pd.read_csv(filename) # this will read the data in as csv format from the txt file and we will then base all of our analysis from this table

#names of variables
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

#data frame code for seperating each species from https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation
#seperating them by species
setosa=df[df['species']=='setosa']
versicolor=df[df['species']=='versicolor']
virginica=df[df['species']=='virginica']

data = str(df.describe())
set = str(setosa.describe())
ver = str (versicolor.describe())
gin = str(virginica.describe())

# check to see if all the species+variables are printed correctly.
#print ("IRIS DATA SET SUMMARY")
#print (data)
#print ("SETOSA DETAILS")
#print(set)
#print ("VERSICOLOR DETAILS")
#print(ver)
#print ("VIRGINICA DETAILS")
#print(gin)


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

# Ref https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation