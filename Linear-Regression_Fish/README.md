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
1. **Loading Dataset** - The tool loads the iris data from the sklearn dataset `load_iris`, then being processed into an array of datapoints, adding a `iris.target`, being the integar representing each class the datapoint is.
2. **Plotting Graphs** - The tool plots graphs showing `sepal length in cm` vs   `sepal width in cm`, and   `petal length in cm` vs `petal width in cm`. Each coloured cluster showing the flower type of each data point.
3. **Create KNN Model** - KNN works by measuring the euclidean distance of the point to its nearest k (in this case 5) neighbors in a multi-dimensional field. The greatest number of k neighbors near the datapoint classifies the data to that category. The data is split into training and testing subsets, then creating the `KNeighborsClassifier`, iterating through the nearest 10 datapoints to the tested point. This model is iterated through 100 times, taking away the data from the highest scoring model (calculated by model accuracy)
4. **Confusion Matrix and Classification** - The confusion matrix compares the class the array predicts, against the true class of the data, a perfectly accurate model would only have a value greater than 0 in each corresponding true value and predicted value. The classification report cacluates precision, recall, F1 Score, and support of the trained classification model.

## Authors
Oscar Ho
17677

## Acknowledgments
* [code-basics](https://youtu.be/CQveSaMyEwM)
