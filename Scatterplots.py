# https://www.educba.com/scatterplots-in-r/
# Descriptive statistics and plots with pandas https://web.microsoftstream.com/video/ecc9ce4a-c6f5-4c50-a4f4-29116fc21b81
# https://pythonbasics.org/seaborn-pairplot/#:~:text=The%20pairplot%20function%20creates%20a,axis%20across%20a%20single%20column.



import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

filename = 'IrisDataSet.txt' # df stands for dataframe
df = pd.read_csv(filename) 



sns.pairplot (df, hue = 'species')

plt.show()

