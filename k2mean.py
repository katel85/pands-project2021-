import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
import matplotlib

# ref https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
# Ref: https://www.youtube.com/watch?v=asW8tp1qiFQ
# Ref: https://web.microsoftstream.com/video/0685eed2-2dd6-490b-b6fc-cda8391f1db7

# for this analysis we imported the iris dataset from sklearn as it is preloaded on
# this library as a dataset array

iris = load_iris()
iris.data
iris.target

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


 
#Visualization of the dataset without alteration of the latter (display of flowers according to their labels)
plt . scatter ( x . Petal_Length , x . Petal_width , c = colormap [ y . Targets ], s = 40 )
plt . title ( 'Actual classification' )
plt . show ()
 
#Visualization of clusters formed by K-Means
plt . scatter ( x . Petal_Length , x . Petal_width , c = colormap [ model . labels_ ], s = 40 )
plt . title ( 'K-means classification' )
plt . show ()