import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import math

def header (msg):
    header('Read Iris Data into a df')
filename = 'IrisDataSet.txt' # df stands for datafile
df = pd.read_csv(filename)

#print(df)

print (df.describe())

# ref: https://www.youtube.com/watch?v=e60ItwlZTKM- Video 


