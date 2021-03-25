import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
col=['sepal_length','sepal_width','petal_length','petal_width','type']
iris=pd.read_csv("Iris.txt",names=col)

print("First five rows")
print(iris.head())
print("*********")
print("columns",iris.columns)
print("*********")
print("shape:",iris.shape)
print("*********")
print("Size:",iris.size)
print("*********")
print("no of samples available for each type") 
print(iris["type"].value_counts())
print("*********")
print(iris.describe())

iris_setosa=iris.loc[iris["type"]=="Iris-setosa"]
iris_virginica=iris.loc[iris["type"]=="Iris-virginica"]
iris_versicolor=iris.loc[iris["type"]=="Iris-versicolor"]

sns.set_style("whitegrid")
sns.pairplot(iris,hue="type",size=3);
plt.show()
