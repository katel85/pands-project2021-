# Jack Caffrey
# PandS Project 2020 Solution
# [#] indicates References which can be viewed in the README

#[4]
import pandas as  pd
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt #Imports the library to save output as PNG file. 

df = pd.read_csv("IrisDataSet.txt") # reads imported CSV file

#[5]
x=df["sepallength"].max()  #Returns the highest value from "Sepal Length"
x1=df["sepallength"].min() #Returns the Lowest value from "Sepal Length"
x2=df["sepallength"].count()  #Returns the total number of records in the coloumn

y=df["sepalwidth"].max()
y1=df["sepalwidth"].min()

z=df["petallength"].max()
z1=df["petallength"].min()

w=df["petalwidth"].max()
w1=df["petalwidth"].min()

Total = (x2) # Defines total number of records in a coloumn in a seperate variable 
New_Total = int(Total/3) # Defines total number of entries per flower type 


#[6]
f = open("Summary.txt","w") #created Summary.txt file and appends to this file
f.write(f"The total number of samples recorded is {Total}. \nThese samples are a combination of 3 sets of {New_Total} Iris flower classes. These classes include: \nSetosa \nVersicolor \nVirginica. \n") # used to display Summary.
f.write(f"The largest value recorded for Sepal Length was {x} the smallest value recorded was {x1} from the {New_Total} samples.\n")
f.write(f"The largest value recorded for Sepal width was {y} the smallest value recorded was {y1} from the {New_Total} samples.\n")
f.write(f"The largest value recorded for Petal Length was {z} the smallest value recorded was {z1} from the {New_Total} samples.\n")
f.write(f"The largest value recorded for Petal Length was {w} the smallest value recorded was {w1} from the {New_Total} samples.\n")
f.write(f" By analysing the Histogram and Scatter plots prodcued by running the program it is possible to categorize each varitation of the flower according to Sepal Length vs Sepal width and Petal Length vs Petal Width.")
f.close() #close Summary.txt

#[7]
sepallenght = (df["sepallength"]) #Reads in data from Sepal Length Column from CVS file.
plt.hist(sepallenght, bins= 20, color = "red") #plots Histogram with column color red
plt.grid(axis='y', alpha=0.5) # Gridlines on for Y axis width determined by alpha value. 
plt.title("Recorded Sepal length (CM)") # Plots Histogram Title
plt.xlabel("Sepal Length") # Plots X axis Title
plt.ylabel("No. of times value is recorded")# Plots Y axis Title
plt.savefig('Sepal Length.png') #Saves Histogram as PNG file. 
plt.show()# displays Histograms.

sepalwidth = (df["sepalwidth"])
plt.hist(sepalwidth, bins= 20, color = "blue") 
plt.grid(axis='y', alpha=0.5)
plt.title("Recorded Sepal Width  (CM)")
plt.xlabel("Sepal Width")
plt.ylabel("No. of times value is recorded")
plt.savefig('Sepal Width.png')
plt.show()

petallength = (df["petallength"])
plt.hist(petallength, bins= 20, color = "orange") 
plt.grid(axis='y', alpha=0.5)
plt.title("Recorded Petal length (CM)")
plt.xlabel("Petal Length")
plt.ylabel("No. of times value is recorded")
plt.savefig('Petal Length.png')
plt.show()


petalwidth = (df["petalwidth"])
plt.hist(petalwidth, bins= 20, color = "green") 
plt.grid(axis='y', alpha=0.5)
plt.title("Recorded Petal Width (CM)")
plt.xlabel("Petal Width")
plt.ylabel("No. of times value is recorded")
plt.savefig('Petal Width.png')
plt.show()

#[4]
plt.scatter(df["sepallength"],df["sepalwidth"])#plots two variables to a scatter plot
plt.title("Petal length vs Petal Width") # Plots Scatter Plot Title
plt.xlabel("Petal Length") # Plots X axis Title
plt.ylabel("Petal Width") # Plots Y axis Title
plt.show()   # displays Scatter plot.

plt.scatter(df["petallength"],df["petalwidth"])
plt.title("Petal length vs Petal Width")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.show() 