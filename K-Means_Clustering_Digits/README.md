
# Predicting hand-written digits using K-Means Clustering

Welcome to the K-NN Classification project. This is an  unsupervised machine learning algorithm for predicting the digit of a handwritten mode, given a 64 bit image of a hand-written digit, using the K-Means Clustering technique. The goal of this program is to predict the digit of a given a matrix of pixel values.

## Description

In this algorithm we are using the digits dataset from [UCI](https://archive.ics.uci.edu/dataset/80/optical+recognition+of+handwritten+digits). The dataset contains data from total of 43 people, 30 contributing to the training set and different 13 to the test set, totaling to 5620 instances. Attributes are the value of each pixel in the 64 bit image.

## Getting Started
### Executing program
The flower species predictor uses K-NN Classification to predict the class of a certain flower based on the attributes, to classify a flower for a new datapoint:
1. **Library Imports** -
  * numpy: for numerical operations
  * sklearn: for machine learning tools
  * matplotlib.pyplot: for data visualization
  * sklearn.cluster: for K-Means clustering
  * sklearn.decomposition: for Principal Component Analysis (dimensionalisation)
  * sklearn.datasets: load digit image data
  * time: for measuring execution time 
  * sklearn: for various evaluation metrics
  * sklearn.pipeline: for creating pipelines
  * sklearn.preprocessing: for data preprocessing

3.  **Loading Dataset** - The tool utilises the `load_digits` function from the `sklearn.datasets` module, the code obtains both the image data and corresponding labels. The number of data points and the number of dimensions (features) are determined from the shape of the data array. 
4. **Define Evaluation Benchmark**  - The evaluation benchmark function records the starting time and constructs a processing pipeline involving data scaling and K-means clustering, fitting it to the input data. The fitting time is calculated, and a results list is initiated to capture evaluation outcomes, encompassing model name, fit time, inertia, clustering evaluation metrics, and silhouette score. These metrics include homogeneity, completeness, V-measure, adjusted Rand score, and adjusted mutual information score, detailing model quality. The silhouette score measures cluster separation. The function then formats and displays the results, a valuable benchmark for comparing K-means performance and aiding parameter and initialisation method selection for clustering tasks.
5. **Running the Benchmark** - The tool employs three distinct methods for initialising the K-means clustering algorithm and evaluates their impact on the clustering results. Firstly, the "k-means++" initialisation method is utilised, which strategically places initial cluster centroids to enhance convergence and improve the quality of the final clusters. Secondly, the "random" initialisation method is employed, which assigns initial centroids randomly. While simple, this method may lead to slower convergence and less optimal cluster configurations due to its sensitivity to initial placement. Lastly, the code explores PCA-based initialisation, involving Principal Component Analysis (PCA) to reduce data dimensionality before clustering. By using PCA-generated components as initial centroids, this method focuses on capturing the most informative aspects of the data. The code's evaluation approach enables a comparative analysis of these methods, shedding light on their individual strengths and weaknesses in achieving effective clustering.
6. **Visualise the results on PCA-reduced data** The tool ilustrates the outcomes of the K-means clustering algorithm on the digit image dataset. The procedure involves reducing the data's dimensionality to two dimensions using Principal Component Analysis (PCA) to enable a comprehensible visualization. Following this, a KMeans instance is initialized using the "k-means++" method, accommodating the predefined number of clusters. This instance is then fitted to the reduced data. The heart of the visualization lies in the definition of a meshgrid that spans the range of the transformed data. Through this meshgrid, the K-means model predicts cluster labels for each point, and these labels are reshaped to align with the meshgrid's shape. The resulting cluster decision boundaries are portrayed as an image. The plot showcases both the original data points, represented as small black dots, and the centroids of the clusters, denoted by white 'X' symbols. This visualization effectively encapsulates the spatial arrangement of clusters in a two-dimensional context, offering insights into the algorithm's proficiency in segmenting digit images. The plot's title provides context, and the set plot limits ensure visual clarity.

## Authors
Oscar Ho
17677

## Acknowledgments
* [TechWithTim - Python Machine Learning: K-Means Clustering](https://youtu.be/i5fIB4Gqaec)
