import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

filename = 'covid.csv'    # df stands for dataframe
df = pd.read_csv(filename)      # this will read the data in as csv format from the txt file and

#print(df)

names = ['Age', 'VitaminD', 'DDimer', 'HospitalLOS',]

data = str(df.describe())
#print(data)

#sns.pairplot (df, hue = 'HospitalLOS')

#plt.figure()
#sns.stripplot(x='VitaminD',y='HospitalLOS',data=df,jitter=True,edgecolor='gray',size=8,palette='winter',orient='v')
#plt.show()

print(df.corr(method='pearson'))

#ref: https://stackoverflow.com/questions/38105539/how-to-convert-a-scikit-learn-dataset-to-a-pandas-dataset

