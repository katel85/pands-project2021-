from sklearn.datasets import load_iris

iris = load_iris()
print(iris)

#data = load_iris()
#df = pd.DataFrame(np.column_stack((data.data, data.target)), columns = data.feature_names+['target'])
#print(df.head())


# ref : https://en.wikipedia.org/wiki/Iris_flower_data_set#:~:text=The%20Iris%20flower%20data%20set,example%20of%20linear%20discriminant%20analysis.
# ref: https://stackoverflow.com/questions/38105539/how-to-convert-a-scikit-learn-dataset-to-a-pandas-dataset
# Due to the fact the Iris Data Set is so often analysed using python is it actually built in to the sklearn datasets. The dataset can be printed out as a data array set.
