
# Predicting hand-written digits using K-Means Clustering

Welcome to the K-NN Classification project. This is an  unsupervised machine learning algorithm for predicting the digit of a handwritten mode, given a 64 bit image of a hand-written digit, using the K-Means Clustering technique. The goal of this program is to predict the digit of a given a matrix of pixel values.

## Description

In this algorithm we are using the digits dataset from [UCI](https://archive.ics.uci.edu/dataset/80/optical+recognition+of+handwritten+digits). The dataset contains data from total of 43 people, 30 contributing to the training set and different 13 to the test set, totaling to 5620 instances. Attributes are the value of each pixel in the 64 bit image.

## Getting Started
### Executing program
The flower species predictor uses K-NN Classification to predict the class of a certain flower based on the attributes, to classify a flower for a new datapoint:
1. **Loading Dataset** - The tool loads the iris data from the sklearn dataset `load_iris`, then being processed into an array of datapoints, adding a `iris.target`, being the integar representing each class the datapoint is.
2. **Plotting Graphs** - The tool plots graphs showing `sepal length in cm` vs   `sepal width in cm`, and   `petal length in cm` vs `petal width in cm`. Each coloured cluster showing the flower type of each data point.
3. **Create KNN Model** - KNN works by measuring the euclidean distance of the point to its nearest k (in this case 5) neighbors in a multi-dimensional field. The greatest number of k neighbors near the datapoint classifies the data to that category. The data is split into training and testing subsets, then creating the `KNeighborsClassifier`, iterating through the nearest 10 datapoints to the tested point. This model is iterated through 100 times, taking away the data from the highest scoring model (calculated by model accuracy)
4. **Confusion Matrix and Classification** - The confusion matrix compares the class the array predicts, against the true class of the data, a perfectly accurate model would only have a value greater than 0 in each corresponding true value and predicted value. The classification report cacluates precision, recall, F1 Score, and support of the trained classification model.

## Authors
Oscar Ho
17677

## Acknowledgments
* [code-basics](https://youtu.be/CQveSaMyEwM)
