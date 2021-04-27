import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
#sklearn 
import sklearn
from sklearn.cluster import KMeans 
from sklearn.preprocessing import scale # for scaling the data
import sklearn.metrics as sm # for evaluating the model
from sklearn import datasets
from sklearn.metrics import confusion_matrix,classification_report

#https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
# code adpted from  https://www.datasciencelearner.com/k-means-clustering-in-python-label-dataset/

rcParams["figure.figsize"] =10,5

iris = datasets.load_iris()
#scale the data
data = scale(iris.data) # scale the iris data
target = pd.DataFrame(iris.target) # define the target 
variable_names = iris.feature_names
data[0:10]

#print(data[0:10])

clustering = KMeans(n_clusters=3,random_state=5)
#fit the dataset
clustering.fit(data)

iris_df = pd.DataFrame(iris.data)
iris_df.columns = ["sepal_length","sepal_width","petal_length","petal_width" ]
target.columns =["Target"]

colors = np.array(["Red","Green","Blue"])
plt.subplot(1,2,1)
plt.scatter(x=iris_df["petal_length"] ,y= iris_df["petal_width"],c = colors[iris.target],s=50)
plt.title("Before K Means Classificaion")

plt.subplot(1,2,2)
plt.scatter(x=iris_df["petal_length"] ,y= iris_df["petal_width"],c = colors[clustering.labels_],s=50)
plt.title("K means Classifcation")
plt.show()


#Both figures suggest that the model has accurately predicted clusters.
#  The only thing you are seeing is the clusters are mislabelled.
#To reassign the Label it uses we use the np.choose() method.
#  To do so you change the label position from [0,1,2] to [2,0,1].

relabel = np.choose(clustering.labels_,[2,0,1]).astype(np.int64)
colors = np.array(["Red","Green","Blue"])
plt.subplot(1,2,1)
plt.scatter(x=iris_df.petal_length ,y= iris_df.petal_width,c = colors[iris.target],s=50)
plt.title("Before K Means Classificaion")

plt.subplot(1,2,2)
plt.scatter(x=iris_df.petal_length ,y= iris_df.petal_width,c = colors[relabel],s=50)
plt.title("K means Classifcation")

plt.show()



