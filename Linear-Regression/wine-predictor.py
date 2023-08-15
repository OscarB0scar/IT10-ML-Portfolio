# Library Imports
import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as pyplot
import pickle
from sklearn import linear_model
from sklearn.utils import shuffle
from matplotlib import style

data = pd.read_csv("winequality-red.data", sep=";")
print(data.head())

data = data[["fixed acidity","volatile acidity","citric acid","residual sugar","chlorides","free sulfur dioxide","total sulfur dioxide","density","pH","sulphates","alcohol"]]
print(data.head())

predict = 'alcohol'

x = np.array(data.drop(predict, axis=1))
y = np.array(data[predict])

# Split the data set into train and test sets
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

linear = linear_model.LinearRegression()

# Define the line of best fit, data is randomly picked from data set
linear.fit(x_train, y_train)
acc = linear.score(x_test, y_test)
print(acc)
