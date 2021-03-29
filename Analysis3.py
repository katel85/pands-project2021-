# Code Ref: https://www.geeksforgeeks.org/plotting-graph-for-iris-dataset-using-seaborn-and-matplotlib/
# Code Ref: https://www.kaggle.com/zachgold/python-iris-data-visualizations


import seaborn as sns

from matplotlib import pyplot as plt
 
iris = sns.load_dataset('iris')
 
# style used as a theme of graph
# for example if we want black
# graph with grid then write "darkgrid"
sns.set_style("whitegrid")
 
# sepal_length, petal_length are iris
# feature data height used to define
# Height of graph whereas hue store the
# class of iris dataset.
sns.FacetGrid(iris, hue ="species",
              height = 6).map(plt.scatter,
                              'sepal_length',
                              'petal_length').add_legend()

plt.show()


sns.boxplot(x="species", y="petal_length", palette="husl", data=iris)
plt.show()