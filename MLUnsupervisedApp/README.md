## Project Overview
The Unsupervised Machine Learning App is an interactive web application built using Streamlit that enables users to experiment with unsupervised machine learning techniques, specifically clustering algorithms. The app allows users to upload their datasets, experiment with three popular clustering models (K-Means, DBSCAN, and Agglomerative Clustering), and visualize the results interactively. Additionally, the app includes performance evaluation metrics like Silhouette Score and Davies-Bouldin Index, and visualization options such as PCA and t-SNE to aid in better understanding and analyzing the clustering results. Users can also export the clustering results and save/load trained models.

## Intructions
1. Install the Required Dependencies: install all the necessary dependencies by running pip install -r requirements.txt

2. Run the App: After installing the dependencies, you can run the app locally using Streamlit. Use the following command: streamlit run /Users/dinahanna/Documents/GitHub/Hanna-Data-Science-Portfolio/MLUnsupervisedApp/StreamlitApp.py

3. Access the App: Once the app is running, open your web browser and go to the following address to view the app: http://localhost:8501

4. Deployed Version:  You can access the deployed version using the link provided: 

## App Features
### 1. Clustering Models
- **K-Means**: A distance-based clustering algorithm that partitions the data into k clusters based on the proximity of data points to centroids.
- **DBSCAN**: A density-based clustering algorithm that identifies clusters based on the density of points, handling noise well.
- **Agglomerative Clustering**: A hierarchical clustering method that builds a tree of clusters through a bottom-up approach.

### 2. Hyperparameter Tuning
- **K-Means**: Users can adjust the number of clusters (n_clusters) for the K-Means algorithm.
- **DBSCAN**: Users can adjust the eps (epsilon) parameter that determines the density threshold for cluster formation.
- **Agglomerative Clustering**: Users can choose the number of clusters (n_clusters) to partition the data.

### 3. Visualization and Metrics
- **PCA**: Visualizes clusters by reducing the data to 2D using **Principal Component Analysis**.
- **t-SNE**: Provides a high-dimensional visualization of clusters using **t-SNE**, preserving the pairwise distances between points.
- **Elbow Plot**: Helps determine the optimal number of clusters for **K-Means** by plotting the within-cluster sum of squares (**WCSS**).
- **Silhouette Score**: Measures how similar each data point is to its own cluster compared to other clusters.
- **Davies-Bouldin Index**: A metric for evaluating cluster separation, where lower values indicate better clustering.

### 4. Data Cleaning
The app allows users to handle missing values by either filling them with the mean/median or dropping rows with missing values.

### 5. Model Saving & Loading
Users can save trained models and load them again for future use without retraining.

## References 
- **[Streamlit](https://docs.streamlit.io/)**
- **[Scikit-learn Documentation](https://scikit-learn.org/stable/)**
- **[t-SNE Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html)**
- **[K-Means Clustering in Scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)**
- **[DBSCAN Clustering in Scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html)**

## Visual Examples
st.image("/mnt/data/Screenshot 2025-05-08 at 3.23.31 PM.png", width=500)

