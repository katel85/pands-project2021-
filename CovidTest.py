import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

filename = 'covid.csv'    
df = pd.read_csv(filename) # this will read the data in as csv format from the txt file and


names = ['Age', 'VitaminD', 'DDimer', 'HospitalLOS','Condition']

data = str(df.describe())

print(data)

# This fictional dataset is has a a high degree of variance. The SD is very high in all 
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

#https://www.datacamp.com/community/tutorials/introduction-machine-learning-python?utm_source=adwords_ppc&utm_campaignid=898687156&utm_adgroupid=48947256715&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=229765585186&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=20487&gclid=Cj0KCQjw9_mDBhCGARIsAN3PaFMqV46OWTzY86tg_8vc0yBOr_Z2-IGgk8fhj_zxq5z-agq1-nRwRbYaAtOeEALw_wcB


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






