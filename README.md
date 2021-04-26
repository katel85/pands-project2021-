# Pands-project2021-G00048625

## Project Brief:

**Problem statement:**

This project concerns the well-known Fisher’s Iris data set. You must research the data set
and write documentation and code in Python to investigate it.Research the data set online and 

[1]. Write a summary about it in your README.

[2]. Download the data set and add it to your repository.

[3]. Write a program called analysis.py that:

- outputs a summary of each variable to a single text file,
-  saves a histogram of each variable to png files, and
- outputs a scatter plot of each pair of variables. 

## Summary of the Fisher's Iris Data Set.

The Fisher Iris Data Set is the measurements of the sepal length and width and petal length and width in centimetres of fifty plants for each of three types of iris; Iris setosa, Iris versicolor and Iris virginica. Although the data were collected by Dr. Edgar Anderson, R. A. Fisher published the data on Iris setosa and Iris versicolor to demonstrate the use of discriminant functions. The Iris virginica data are used to extend Fisher’s technique and to test Randolph’s (1934) hypothesis that Iris versicolor is a polyploid hybrid of the two other species which is related to the fact that Iris setosa is a diploid species with 38 chromosomes, Iris virginica a tetraploid and Iris versicolor having 108 chromosomes is a hexaploid.



![](IRIS%20FLOWERS.png)

**What is Linear Discriminant Analysis:**

Fisher's Iris data has become a popular set of labeled data for testing—and especially for comparing—clustering algorithms and classifiers. It is, of course, entirely appropriate and in the spirit of scientific inquiry to make and publish comparisons of models and their performance on common data sets and the pattern recognition community has used Iris in perhaps a thousand papers for just this reason.

Linear Discriminant Analysis(LDA) is a very common technique used for supervised classification problems. Lets understand what is LDA and how does it work.

Linear Discriminant Analysis is a dimensionality reduction technique used as a preprocessing step in Machine Learning and pattern classification applications. The main goal of dimensionality reduction techinques is to reduce the dimensions by removing the reduntant and dependent features by transforming the features from higher dimensional space to a space with lower dimensions. In simple terms, discriminant function analysis is classification - the act of distributing things into groups, classes or categories of the same type.

**What is Python and what is it used for:**

Python is a popular multi-purpose programming language widely used for its flexibility, as well as its extensive collection of libraries, which are valuable for analytics and complex calculations.Python’s extensibility means that it has thousands of libraries dedicated to analytics, including the widely used Python Data Analysis Library (also known as Pandas).For the most part, data analytics libraries in Python are at least somewhat derived from the NumPy library, which includes hundreds of mathematical calculations, operations, and functions. For this project Python version used was 3.8.5.

Python is a general-purpose coding language—which means that, unlike HTML, CSS, and JavaScript, it can be used for other types of programming and software development besides web development. That includes back end development, software development, data science and writing system scripts among other things. 

The application we used Python for in this course was scripting and data science. The  objective of this course was to become comfortable with coding and used the python languauge to do this.Even though python is versatile and powerful its is relatively easy to  learn the lauguage. Several reasons for this are:

- Python basics (things like Python’s syntax, keywords, and data types) can be learned in as little as 6-8 weeks.
- You can learn python basics for free. There are several python sites such as the python software foundation that offer free tutorials for beginners.
- Python has a massive support community and is an open source coding language.Being open-source is what allows languages to have libraries, frameworks, and other tools that keep the Python language relevant and adaptable over time. But open-source only lives up to its potential if there’s a supportive community of users engaged with the language.
- Being general-purpose means the Python language can do a lot…which is why heavy tech hitters like Google, Facebook, and Instagram all use Python programming to build parts of their tech stacks.Python’s versatility means that you’ll have an incredibly wide range of work options.
- Automation is another area where it pays to learn Python. Python’s ability to write system scripts means you can create simple Python programs to automate mindless tasks that eat away at your productivity. The time you’ll save by knowing how to automate processes with Python is a huge selling point for learning the language.


## Analysing Fisher's Iris Dataset Using Python

**Applications used:**

CMDER- CMDER is a free software package, portable console emulator specifically for Windows. CMDER is a great utility for developers and coders. It is used primarily for running scripts but has many more functions. I cloned my respiratory for the project from github through cmder and saved it onto my machine.

VSCODE- Visual Studio Code is a freeware source-code editor made by Microsoft for Windows, Linux and macOS. All code for this project was written though this application. It is an amazing platform for someone beginning their programming/scripting journey as it is incredibly user friendly.

GITHUB-GitHub is a cloud-based hosting service that lets you manage Git repositories. If you have open-source projects that use Git, then GitHub is designed to help you better manage them. This was used to store all the code that was written and the overall project. The beauty is that yu can access this cloud base service from any machine. Ref :https://guides.github.com/introduction/git-handbook/#:~:text=GitHub%20is%20a%20Git%20hosting,apps%20in%20the%20GitHub%20Marketplace.

# Dataset Code and Analysis:

**Libraries Used:**

In order to analyse and visualize the Iris Dataset in VSCODE we  installed several libraries. A library is a collection of pre-combined codes that can be used iteratively to reduce the time required to code. They are particularly useful for accessing the pre-written frequently used codes, instead of writing them from scratch every single time. Similar to the physical libraries, these are a collection of reusable resources, which means every library has a root source. This is the foundation behind the numerous open-source libraries available in Python. Ref: https://www.mygreatlearning.com/blog/open-source-python-libraries/#Library

**Matplotlib**-is a comprehensive library for creating static, animated, and interactive visualizations in Python"

**Numpy**-is a general-purpose array-processing package. It provides a high-performance multidimensional array object, and tools for working with these arrays. It is the fundamental package for scientific computing with Python.

**Pandas**-is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.

**Seaborn**- is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.



**Dataset Download and Import:**

The start of analysis requires us to download this Iris dataset. This was taken from UCI Machine Learning Respository. The data was downloaded from the Data Folder on this site through notepad and then saved as a csv file. I saved this in my pands-project folder in csv and txt format.Due to the fact the Iris Data Set is so often analysed using python is it actually built in to the sklearn datasets which is another library that you can import. The dataset can be printed out as a data array set. Why researching the dataset I dounf another way to download the dataset was through Seaborn as this has built in datasets also. Seaborn is part of the PyData stack hence accepts Pandas’ data structures. However the brief of this project was to download so that is what we did. The dataset was defined as filename and then read in using the pandas lib and defined as df.


![](Plots/IrisDatasetImport.png)



## Summary of each variable:

The describe() function computes a summary of statistics pertaining to the DataFrame columns.

The three species were also separately defined to get their summary statistics also.

![](Plots/Summaryoutput.png)


## Histogram of each variable type:

The Histograms show us the range in centimetres(cm) for each of the variables and the frequency these occur in the dataset. The code written showed histograms for each individual variable. The second type of histogram code written was for each variable but species specific. Finally code was written for distplots which I think represented the data in a manner that variables could be differenciated per species if the data points were distinguishable.


![](Plots/Variable_Histograms.png)


Looking at the overall distribution above, petal length and petal width does not have a normal distribution, whereas sepal length and sepal width are uniformly distributed.

![](Plots/Petal_Length%20Distplot.png)

Using the displot above of petal length Iris.Setosa is easily disguishable from the other two species. There is a slight overlap on virginica and versicolor but ditinct distributions nonetheless.

![](Plots/Petal_Width%20Distplot.png)

Using this displot of petal width. Iris setosa is again easily identified. There is overlap again with Versicolor and Virginica. 

It would be correct to assume we could use this analysis to definitively separate setosa from the other two however you would need further analysis to distinguish between Virginica and Versicolor.


## Scatterplots of each Pair of Variables:

Scatterplots show how much one variable is affected by another. The relationship between two variables is called their correlation. The closer the data points come when plotted to making a straight line, the higher the correlation between the two variables, or the stronger the relationship. The initial scatterplot code generated the entire data and was not species specific. 



![](Plots/Scatterplot%20PairVar%20Species.png)

The second scatter plot generated is seen above. Here the code is species specific and Iris Setosa is easily distinguished from The other two species. The petal width and length scatterplot is better at distinguishing the three species type although there is some over lap between Iris Vericolour and Iris Virginica.

![](Plots/Correlationstats.png)

The above figure shows the correlation statistics between all the variable. Perfect positive correction would produce a number of 1. As seen above when the variable is compared against itself. However there are three main variables with high positive correlation.


  [1] Petal Width and Petal Length (0.96)

  [2] Petal Length and Sepal Length (0.87)

  [3] Petal Width and Sepal Length (0.81)


  ![](Plots/regplotpetalpetal.png)

  The lmplot in the seaborn module above shows the high degree of correlation between the petal length and width. This plot is used to visualize a linear relationship as determined through regression.The figure will draw a scatterplot of two variables, x and y, and then fit the regression model y ~ x and plot the resulting regression line and a 95% confidence interval for that regression:

  ![](Plots/regplotpetalsepal.png)

  The lmplot above shows the two variables that showed the least correlation. The sepal width and the petal length. 
 
![](Plots/sns.pairplot.png)

The pairplot generated above is incredibly descriptive and pairs all variables together. It is interesting to see how the scatterplot will change when the same variables are used in the scatterplot but placed on different axis. In every paired plot here Iris setosa can be easily identified among the other two species.

Observations:

- Petal_length and petal_width are the most useful features to identify various flower types.
- While Setosa can be easily identified (linearly separable), Virginica and Versicolor have some overlap (almost linearly separable).

































**References:**

What is Python for Data Analysis? 

<https://www.sisense.com/glossary/python-for-data-analysis/>

Iris Data <https://link.springer.com/chapter/10.1007/978-1-4612-5098-2_2>
<https://skillcrush.com/blog/what-is-python/>

<https://www.markdownguide.org/basic-syntax/>











