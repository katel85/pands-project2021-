import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
import matplotlib as plt
import pylab as plt
import numpy as np
import sklearn.metrics as sm

# ref https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
# Ref: https://www.youtube.com/watch?v=asW8tp1qiFQ
# Ref: https://web.microsoftstream.com/video/0685eed2-2dd6-490b-b6fc-cda8391f1db7

# for this analysis we imported the iris dataset from sklearn as it is preloaded on
# this library as a dataset array

iris = load_iris()
iris.data
iris.target

x = pd.DataFrame(iris.data, columns=['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'])
y = pd.DataFrame(iris.target, columns=['Target'])

#print(x)
print(y)

#print(iris)- this shows me the dataset in array format
#print (iris.data)-this will show me just the data set in the array
#print(iris.target)- this will show me the targets labelled as [0,1,2]- corresponds to species-caregorically variable 

kmeans= KMeans(n_clusters=3) # we specify the amount of clusters

KMmodel = kmeans.fit(iris.data) # using the predefined kmeans algorithm we will fit a model of the iris data

KMmodel.labels_  # this is our predicted category according to our model
#print (KMmodel.labels_)- you can see here the misclassification in virginica and versicolor
KMmodel.cluster_centers_

pd.crosstab(iris.target,KMmodel.labels_)
#print(pd.crosstab(iris.target,KMmodel.labels_))
# the crosstab shows exactly how many of each species is misclassified and 
# 14 out of 50 of the Iris virginica are misclassified as iris versicolor using this model.

#accuracy_score(iris.target,KMmodel_labels_) 
#print (accuracy_score(iris.target,KMmodel_labels_))

#Accuracy is the sum of correct observation by the total observation
Accuracy=(50+48+36)/150
print(Accuracy)
# accuracy from this model of predicting the correct species is 0.893
# the k-means algorithm did a good job is clustering the data and
#predicting the species based on this.

#Ref: https://github.com/venky14/# Machine-Learning-with-Iris-Dataset/blob/master
# /Machine%20Learning%20with%20Iris%20Dataset.ipynb

# https://github.com/bhattbhavesh91/k_means_iris_dataset/blob/master/K_means_with_Iris_Data.ipynb
# ref https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

#ref: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
# http://stamfordresearch.com/k-means-clustering-in-python/

#Start with a plot figure of size 12 units wide & 3 units tall
plt.figure(figsize=(12,3))

# Create an array of three colours, one for each species.
colors = np.array(['red', 'green', 'blue'])

# make sure the array is in the correct order {2,0,1} so it will appear is the correct order in the plt
predictedY = np.choose(KMmodel.labels_, [2, 0, 1]).astype(np.int64)

# Plot the classifications that we saw earlier between Petal Length and Petal Width
plt.subplot(1, 2, 1)
plt.scatter(x['Petal Length'], x['Petal Width'], c=colors[iris.target], s=40)
plt.title('Before classification')
 
# Plot the classifications according to the model
plt.subplot(1, 2, 2)
plt.scatter(x['Petal Length'], x['Petal Width'], c=colors[predictedY], s=40)
plt.title("Model's classification")
plt.show()

sm.accuracy_score(iris.target, predictedY)

print(sm.accuracy_score(iris.target, predictedY))

#sm.confusion_matrix(predictedY,iris.target)

#print(sm.confusion_matrix(predictedY,iris.target))
#We can see that all the red dots are grouped/clustered 100% accurately and the green and black dots are fairly 
# well grouped too.

#Ref: https://github.com/venky14/# Machine-Learning-with-Iris-Dataset/blob/master
# /Machine%20Learning%20with%20Iris%20Dataset.ipynb

# https://github.com/bhattbhavesh91/k_means_iris_dataset/blob/master/K_means_with_Iris_Data.ipynb
# ref https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

#ref: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
# http://stamfordresearch.com/k-means-clustering-in-python/


