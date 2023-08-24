# Predicting fish weight using linear regression

Welcome to the lienar regression project. This is a supervised machine learning algorithm for predicting  fish weight, given lengths, height, and width, using the linear regression technique. The goal of this program is to predict the weigth of a given fish, based on cross length, diagonal length, vertical length, diagonal length, height and width. 

## Description

In this algorithm we are using the fish market dataset from [kaggle](https://www.kaggle.com/datasets/aungpyaeap/fish-market). The dataset contains regarding 7 common market fish. Attributes include Species, Weight, Length1, Length2, Length3, Height and Width.

## Getting Started
### Executing program
The fish weight predictor uses Linear Regression to predict the weight of a fish based on the attributes, to predict the weight for a new datapoint:
* Species
* Weight
* Length1
* Length2
* Length3
* Height
* Width
1. **Library Imports**
  * pandas: Used for data manipulation and analysis
  * numpy : Numpy is the core library for scientific computing in Python. It is  used for working with arrays and matrices.
  * sklearn: tools for predictive data analysis
  * linear_model: Sklearn linear regression model
  * matplotlib: It’s plotting library, and we are going to use it for data       visualization
  * Pickle: the process of converting a Python object into a byte stream to store it in a file/database, maintain program state across sessions, or transport data over the network
  * style: styling the graph
3. **Loading Dataset** - The tool reads the csv file `Fish.csv`, and then filters a set of variables that are usable (integar or float values), so we will be excluding `Species`, and we well set the value of each datapoint to predict as `Weight `.
4. **Training the linear regression model** - The tool splits the data into training and testing variables, then creates a linear regression model using `linear_model.LinearRegression()`. The tool will take data from the highest accuracy model by itterating through this function 100 times. Linear regression works by drawing a line of best fit through a multi-dimensional field, and then predicting new datapoints using the line of best fit. 
5. **Displaying Predicted data vs Actual data** - The tool displays the predicted data and the actual data of the top trained model, the accuracy, the 
6. **Create KNN Model** - KNN works by measuring the euclidean distance of the point to its nearest k (in this case 5) neighbors in a multi-dimensional field. The greatest number of k neighbors near the datapoint classifies the data to that category. The data is split into training and testing subsets, then creating the `KNeighborsClassifier`, iterating through the nearest 10 datapoints to the tested point. This model is iterated through 100 times, taking away the data from the highest scoring model (calculated by model accuracy)
7. **Confusion Matrix and Classification** - The confusion matrix compares the class the array predicts, against the true class of the data, a perfectly accurate model would only have a value greater than 0 in each corresponding true value and predicted value. The classification report cacluates precision, recall, F1 Score, and support of the trained classification model.

## Authors
Oscar Ho
17677

## Acknowledgments
* [code-basics](https://youtu.be/CQveSaMyEwM)
