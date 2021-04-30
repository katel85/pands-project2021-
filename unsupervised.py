import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
import pylab as plt
import numpy as np
import sklearn.metrics as sm

sns.set() # set the default seaborn theme, scaling, and color palette.
# code here is written for the sepal length and sepal width on a scatter plot with no species label. No pattern can be detected.
# the second scatterplot of unlabelled petal length and petal width you can see a linear  cluster pattern from the data even though it is unlabelled.
# code adpted from https://shunsvineyard.info/2017/10/22/machine-learning-basics-and-perceptron-learning-algorithm/
filename = 'IrisDataSet.txt' 
df = pd.read_csv(filename) 
unlabeled_data = df.iloc[:, [0,1,2,3]].values #iloc() function accepts only integer type values as the index 
#print (df)
#print(unlabeled_data)
#names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
plt.figure(figsize=(12,3))
plt.subplot(1, 2, 1)
plt.scatter(unlabeled_data[:, 0], unlabeled_data[:, 1],
            color="magenta", marker="o")
plt.xlabel("sepal length")
plt.ylabel("sepal width")
plt.legend(loc="upper left")
plt.title("Sepal Length & Width Unsupervised")
plt.subplot(1, 2, 2)
plt.scatter(unlabeled_data[:, 2], unlabeled_data[:, 3],
            color="g", marker="o")
plt.xlabel("petal length")
plt.ylabel("petal width")
plt.legend(loc="upper left")
plt.title("Petal Length & Width Unsupervised")
plt.show()

# code here is written for the sepal length and sepal width on a scatter plot with no species label. No pattern can be detected.
# the second scatterplot of unlabelled petal length and petal width you can see a linear  cluster pattern from the data even though it is unlabelled.
# what the code above shows us is that is is hard to see the clusters and associations when the data is not 
# labelled(i.e not supervised). Due to the fact that species used as a tag in the code we would not be interpreted the 
# same way as if it were labelled with species
# Clustering is an important concept when it comes to unsupervised learning. 
# It mainly deals with finding a structure or pattern in a collection of uncategorized data. 
# Clustering algorithms will process your data and find natural clusters(groups) if they exist in the data. 
# You can also modify how many clusters your algorithms should identify. It allows you to adjust the granularity of 
# these groups. There are different types of clustering you can utilize one of these is k-means clustering.


# for this analysis we imported the iris dataset from sklearn as it is preloaded on
# this library as a dataset array
#pylint: disable=no-member
#had to use above statement as I kept getting tuple errors on the code for iris
iris = load_iris()
iris.data
iris.target
print(iris.target)
#print(iris)- this shows me the dataset in array format
#print (iris.data)-this will show me just the data set in the array
#print(iris.target)- this will show me the targets labelled as [0,1,2]- corresponds to species-caregorically variable 


kmeans= KMeans(n_clusters=3) # we specify the amount of clusters- we know there are 3 cluster in the iris set. If we didn't
#know this we could set the cluster number to whatever we felt it might be??
KMmodel = kmeans.fit(iris.data) # using the predefined kmeans algorithm we will fit a model of the iris data
# this is our predicted category according to our model
KMmodel.labels_  
KMmodel.cluster_centers_
print (KMmodel.labels_) #you can see here the misclassification in virginica and versicolor
print(KMmodel.cluster_centers_)
# this is our predicted category according to our model
#print (KMmodel.labels_)- you can see here the misclassification in virginica and versicolor
# the crosstab shows exactly how many of each species is misclassified and 
# 14 out of 50 of the Iris virginica are misclassified as iris versicolor using this model.
pd.crosstab(iris.target,KMmodel.labels_)
print(pd.crosstab(iris.target,KMmodel.labels_))
# the crosstab shows exactly how many of each species is misclassified and 
# 14 out of 50 of the Iris virginica are misclassified as iris versicolor using this model.


#Accuracy is the sum of correct observation by the total observation
Accuracy=(50+48+36)/150
print(Accuracy)
# accuracy from this model of predicting the correct species is 0.893
# the k-means algorithm did a good job is clustering the data and
#predicting the species based on this.


# Now I want to put this code into a scatter plot to show the actaul classification and predicted classification
# code adapted from https://constantgeeks.com/2017/01/11/playing-with-iris-data-kmeans-clustering-in-python/
x = pd.DataFrame(iris.data, columns=['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'])
#y = pd.DataFrame(iris.target, columns=['Target'])

#print(x)
#print(y)

plt.figure(figsize=(12,3))

# Create an array of three colours, one for each species.
colors = np.array(['blue', 'indigo', 'crimson'])

# make sure the array is in the correct order {2,0,1} so it will appear is the correct order in the plt
predictedY=KMmodel.labels_
#predictedY = np.choose(KMmodel.labels_, [2, 0, 1]).astype(np.int64)

# Plot the classifications that we saw earlier between Petal Length and Petal Width
plt.subplot(1, 2, 1)
plt.scatter(x['Petal Length'], x['Petal Width'], c=colors[iris.target], s=50)
plt.title('Before K-Mean Model Classification')
 
# Plot the classifications according to the model
plt.subplot(1, 2, 2)
plt.scatter(x['Petal Length'], x['Petal Width'], c=colors[predictedY], s=50)
plt.title(" After K-Mean Model Classification")
plt.show()

sm.accuracy_score(iris.target, predictedY)

print(sm.accuracy_score(iris.target, predictedY))

sm.confusion_matrix(iris.target, predictedY)

print(sm.confusion_matrix(iris.target, predictedY))
#We can see that all the red dots are grouped/clustered 100% accurately and the green and black dots are fairly 
# well grouped too.

# https://github.com/venky14/# Machine-Learning-with-Iris-Dataset/blob/master/Machine%20Learning%20with%20Iris%20Dataset.ipynb
# https://github.com/bhattbhavesh91/k_means_iris_dataset/blob/master/K_means_with_Iris_Data.ipynb
# https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
# https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
# http://stamfordresearch.com/k-means-clustering-in-python/
# https://www.datasciencemadesimple.com/harmonic-mean-function-python-pandas-dataframe-row-column-wise/
# https://www.youtube.com/watch?v=asW8tp1qiFQ
# https://web.microsoftstream.com/video/0685eed2-2dd6-490b-b6fc-cda8391f1db7
# https://github.com/shunsvineyard/shunsvineyard/blob/main/machine-learning-basics-and-perceptron-learning-algorithm/unsupervised.py

