import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

# ref https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

# then the preloaded iris set is read in with panda and defined as x
x = pd.DataFrame(iris.data)
# we now define the columns of the df with the variable names 
x.columns = ['Sepal_Length','Sepal_width','Petal_Length','Petal_width']

y = pd.DataFrame(iris.target)


y.columns = ['Targets']


#Création d'un objet K-Means avec un regroupement en 3 clusters (groupes)
model=KMeans(n_clusters=3)



#application du modèle sur notre jeu de données Iris
model.fit(x)



#Visualisation des clusters
plt.scatter(x.Petal_Length, x.Petal_width)
plt.show()




colormap=np.array(['Red','green','blue'])



#Visualisation du jeu de données sans altération de ce dernier (affichage des fleurs selon leur étiquettes)
plt.scatter(x.Petal_Length, x.Petal_width,c=colormap[y.Targets],s=40)
plt.title('Classification réelle')
plt.show()

#Visualisation des clusters formés par K-Means
plt.scatter(x.Petal_Length, x.Petal_width,c=colormap[model.labels_],s=40)
plt.title('Classification K-means ')
plt.show()

#ref: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html