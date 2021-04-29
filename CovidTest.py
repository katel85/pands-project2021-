import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

filename = 'covid.csv'    # df stands for dataframe
df = pd.read_csv(filename)      # this will read the data in as csv format from the txt file and

#print(df)

HeartDisease=df[df['Condition']=='HeartDisease']
Asthmatic=df[df['Condition']=='Asthmatic']
NoCondition=df[df['Condition']=='NoCondition']

names = ['Age', 'VitaminD', 'DDimer', 'HospitalLOS','Condition']

data = str(df.describe())
#print(data)

sns.pairplot (df, hue = 'Condition')
#plt.show()

#plt.figure()
#sns.stripplot(x='Age',y='HospitalLOS',data=df,jitter=True,edgecolor='gray',size=8,palette='winter',orient='v')
#plt.show()

print(df.corr(method='pearson'))

#ref: https://stackoverflow.com/questions/38105539/how-to-convert-a-scikit-learn-dataset-to-a-pandas-dataset

plt.figure(figsize=(7,4)) 
sns.heatmap(df.corr(),annot=True)
#plt.show()

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

figboxplot, (ax1, ax2,) = plt.subplots(1,2, figsize=(13,10)) 
sns.boxplot(x="Condition", y="Age", data=df, ax=ax1)
sns.swarmplot(x="Condition", y="Age", data=df, color="k", ax=ax1)
ax1.set_ylabel("Age", color="g")
ax1.set_xlabel("Age", color='r')

sns.boxplot(x="Condition", y="VitaminD", data=df, ax=ax2)
sns.swarmplot(x="Condition", y="VitaminD", data=df, color="k", ax=ax2)
ax2.set_ylabel("VitaminD")  
ax2.set_xlabel("VitaminD", color='r')
plt.show()



#plt.savefig("CovidBoxPlots")





