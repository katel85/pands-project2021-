import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
import seaborn as sns

#https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/ 
#http://www.cse.msu.edu/~ptan/dmbook/tutorials/tutorial3/tutorial3.html
# For multivariate statistics, you can compute the covariance and correlation between pairs of attributes
filename = 'IrisDataSet.txt' # df stands for dataframe
df = pd.read_csv(filename) # this will read the data in as csv format from the txt file and we will then base all of our analysis from this table

#names of variables
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# Correlation between variables
print(df.corr(method='pearson'))

# Co Variance between 
print (df.cov())


