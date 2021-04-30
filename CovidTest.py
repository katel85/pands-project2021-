import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

filename = 'covid.csv'    # df stands for dataframe
df = pd.read_csv(filename)      # this will read the data in as csv format from the txt file and


names = ['Age', 'VitaminD', 'DDimer', 'HospitalLOS','Condition']

data = str(df.describe())

print(data)

# This fictional dataset is has a ahigh degree of variance. The SD is very high in all 
# the variables meaning the data is not clustered around the mean and is spread out.
# While I could go back and change the data we will continue and see what kind of plots we will
# see when the data reveals.
# 
# I did a pairplot of all the varibles against each other with Condition as the Hue. This revealed 
# the patients condition could be differenciated using the variables. People with heart disease were
# older stayed longer in hospital and lower Vit D leveles and higher DDimer levels. Patients with asthma 
# stayed in hospital for a shorter length of time then patients with heart disease but still longer 
# than patients with no condition. It was clear from the pairplot people with no underlying health conditions
# stayed in hospital for a shorter length of time has better Vitamin D levels and low DDimer levels.

sns.pairplot (df, hue = 'Condition',palette = ["deeppink","g","b"])
plt.show()

print(df.corr(method='pearson'))

# we looked at the correlation between the variables.

#ref: https://stackoverflow.com/questions/38105539/how-to-convert-a-scikit-learn-dataset-to-a-pandas-dataset

plt.figure(figsize=(7,4)) 
sns.heatmap(df.corr(),annot=True)
#plt.show()

#The heatmap is a very quick way to visualize the correlation between the variables.

#https://blog.quantinsti.com/creating-heatmap-using-python-seaborn/

plt.figure()
sns.regplot(x=df["Age"], y=df["HospitalLOS"], line_kws={"color":"r","alpha":0.7,"lw":5})
#plt.show()

plt.figure()
sns.regplot(x=df["VitaminD"], y=df["HospitalLOS"], line_kws={"color":"r","alpha":0.7,"lw":5})
#plt.show()

sns.set(style='whitegrid')
sns.swarmplot(x="Condition", y="HospitalLOS", data=df)
plt.show()

#code adapted from https://www.geeksforgeeks.org/swarmplot-using-seaborn-in-python/

figboxplot, (ax1, ax2,) = plt.subplots(1,2, figsize=(11,9)) 
sns.boxplot(x="Condition", y="Age", data=df, ax=ax1)
sns.swarmplot(x="Condition", y="Age", data=df, color="k", ax=ax1)
ax1.set_ylabel("Age", color="g")
ax1.set_xlabel("Condition", color='r')

sns.boxplot(x="Condition", y="VitaminD", data=df, ax=ax2)
sns.swarmplot(x="Condition", y="VitaminD", data=df, color="k", ax=ax2)
ax2.set_ylabel("VitaminD")  
ax2.set_xlabel("Condition", color='r')
plt.show()

#code adapted from ref: https://onestopdataanalysis.com/box-and-plot-whisker/






