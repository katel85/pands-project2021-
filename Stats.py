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

#https://www.datacamp.com/community/tutorials/introduction-machine-learning-python?utm_source=adwords_ppc&utm_campaignid=898687156&utm_adgroupid=48947256715&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=229765585186&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=20487&gclid=Cj0KCQjw9_mDBhCGARIsAN3PaFMqV46OWTzY86tg_8vc0yBOr_Z2-IGgk8fhj_zxq5z-agq1-nRwRbYaAtOeEALw_wcB
#https://medium.com/analytics-vidhya/linear-regression-using-iris-dataset-hello-world-of-machine-learning-b0feecac9cc1