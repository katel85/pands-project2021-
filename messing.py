import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

filename = 'IrisDataSet.txt'    # df stands for dataframe
df = pd.read_csv(filename)      # this will read the data in as csv format from the txt file and
# we will then base all of our analysis from this table.

#KDE can produce a plot that is less cluttered and more interpretable, especially when drawing multiple distributions.


setosa=df[df['species']=='setosa']
versicolor=df[df['species']=='versicolor']
virginica=df[df['species']=='virginica']

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


#https://seaborn.pydata.org/tutorial/distributions.html
# https://towardsdatascience.com/how-to-use-seaborn-for-data-visualization-4c61fc488ec1





