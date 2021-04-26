 #matplotlib is a python 2D plotting library which produces publication
# quality. Figures in a variety of hardcopy formats and interactive
# environments across platforms.
# http://matplotlib.org/2.0.0/index.html
import matplotlib.pyplot as plt

# pandas is an open source library providing high-performance, 
# easy-to-use data structures and data analysis tools.
# http://pandas.pydata.org/
import pandas as pd

# Seaborn is a Python data visualization library based on matplotlib.
# It provides a high-level interface for drawing attractive and
# informative statistical graphics.
# http://seaborn.pydata.org/index.html
import seaborn as sns

sns.set() # set the default seaborn theme, scaling, and color palette.


filename = 'IrisDataSet.txt' 
df = pd.read_csv(filename) 
unlabeled_data = df.iloc[:, [0, 2]].values

#names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

plt.scatter(unlabeled_data[:, 0], unlabeled_data[:, 1],
            color="green", marker="o")

plt.xlabel("sepal length")
plt.ylabel("petal length")
plt.legend(loc="upper left")
plt.show()


# ref: https://github.com/shunsvineyard/shunsvineyard/blob/main/machine-learning-basics-and-perceptron-learning-algorithm/unsupervised.py