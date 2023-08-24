# Predicting iris flower using K-NN Classification

Welcome to the K-NN Classification project. This is a supervised machine learning algorithm for predicting the flower species of a flower, given petal and sepal lengths, using the K-NN Classification technique. The goal of this program is to predict the species of a given flower, based on sepal length, sepal width, petal length, and petal width. 

## Description

In this algorithm we are using the iris dataset from [sklearn toy datasets ]([https://archive.ics.uci.edu/ml/datasets/Student+Performance](https://scikit-learn.org/stable/datasets/toy_dataset.html)). The dataset contains data from 50 * 3 instances, 1 for each class of flower. Attributes include: sepal length in cm, sepal width in cm, petal length in cm, and petal width in cm.

## Getting Started
### Executing program
The flower species predictor uses K-NN Classification to predict the class of a certain flower based on the attributes, to classify a flower for a new datapoint:
* sepal length in cm
* sepal width in cm
* petal length in cm
* petal width in cm
1. **Loading Dataset** - The tool loads the iris data from the sklearn dataset `load_iris`, then being processed into an array of datapoints, adding a `iris.target`, being the integar representing each class the datapoint is.
2. **Plotting Graphs** - The tool plots graphs showing `sepal length in cm` vs   `sepal width in cm`, and   `petal length in cm` vs `petal width in cm`. Each coloured cluster showing the flower type of each data point.
3. **Create KNN Model** - KNN works by measuring the euclidean distance of the point to its nearest k (in this case 5) neighbors in a multi-dimensional field. The greatest number of k neighbors near the datapoint classifies the data to that category. The data is split into training and testing subsets, then creating the `KNeighborsClassifier`, iterating through the nearest 10 datapoints to the tested point. This model is iterated through 100 times, taking away the data from the highest scoring model (calculated by model accuracy)
4. **Confusion Matrix and Classification** - The confusion matrix compares the class the array predicts, against the true class of the data, a perfectly accurate model would only have a value greater than 0 in each corresponding true value and predicted value. The classification report cacluates precision, recall, F1 Score, and support of the trained classification model.



## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

ex. Dominique Pizzie  
ex. [@DomPizzie](https://twitter.com/dompizzie)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
