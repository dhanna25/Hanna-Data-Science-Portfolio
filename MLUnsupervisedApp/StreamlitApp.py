
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, davies_bouldin_score
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.manifold import TSNE

# Streamlit App Setup
st.set_page_config(page_title="Advanced Unsupervised ML App", layout="wide")

# Title and Description
st.title("Advanced Unsupervised Machine Learning Exploration")
st.markdown("""
Upload a dataset, experiment with multiple clustering models, and visualize the results interactively.
This app includes K-Means, DBSCAN, and Agglomerative Clustering, with various performance metrics.
""")

# Sidebar for Dataset Selection and Hyperparameters
st.sidebar.header("Settings")
uploaded_file = st.sidebar.file_uploader("Upload your dataset (CSV)", type=["csv"])

# Sample datasets for user selection
sample_data = st.sidebar.selectbox("Or select a sample dataset", ["Iris", "Wine", "Digits", "None"])

# Add an expander for Dataset Summaries
with st.expander("Dataset Summaries"):
    st.write("""
    ### 1. Iris Dataset
    The **Iris dataset** contains 150 samples of iris flowers with four features: sepal length, sepal width, petal length, and petal width. These features are used to classify the flowers into three species: Setosa, Versicolor, and Virginica. This dataset is commonly used for classification and clustering tasks.

    ### 2. Wine Dataset
    The **Wine dataset** consists of 178 samples of wine with 13 chemical features, including alcohol content, color intensity, and flavonoids. The dataset is divided into three classes, each corresponding to a different wine cultivar. This dataset is useful for classification and clustering tasks based on the chemical properties of wine.

    ### 3. Digits Dataset
    The **Digits dataset** contains 1,797 grayscale images of handwritten digits (0-9). Each image is 8x8 pixels in size, with 64 features per image. The dataset is commonly used for classification and clustering tasks, especially for digit recognition and image processing.

    ### 4. Custom User-uploaded Dataset
    Users can upload their own datasets in CSV format. These datasets can contain any number of features and samples, and the app will automatically handle preprocessing and clustering. The ability to upload custom datasets provides flexibility for different use cases.
    """)

# Default dataset loading
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(f"Dataset Shape: {df.shape}")
    st.write("Dataset preview:")
    st.write(df.head())
    
    # Data Cleaning
    with st.expander("Data Cleaning"):
        st.write("""
        In this section, we check for missing values and duplicates. Missing values can be handled by either filling them 
        with the mean or median of the column or dropping rows that contain missing values. 
        Duplicates are also checked and can be removed to ensure the quality of your dataset before clustering.
        """)
    
    # Check for missing values
    missing_values = df.isnull().sum()
    st.write("Missing Values by Column:")
    st.write(missing_values)
    
    # Option to fill missing values or drop rows
    fill_missing = st.sidebar.radio("How would you like to handle missing values?", ["Fill with Mean", "Fill with Median", "Drop rows with Missing Values"])
    if fill_missing == "Fill with Mean":
        df = df.fillna(df.mean())
    elif fill_missing == "Fill with Median":
        df = df.fillna(df.median())
    elif fill_missing == "Drop rows with Missing Values":
        df = df.dropna()

    # Check for duplicates
    st.write("Checking for duplicate rows:")
    duplicates = df.duplicated().sum()
    st.write(f"Number of duplicate rows: {duplicates}")
    remove_duplicates = st.sidebar.checkbox("Remove Duplicate Rows", value=True)
    if remove_duplicates:
        df = df.drop_duplicates()
    
elif sample_data == "Iris":
    from sklearn.datasets import load_iris
    data = load_iris()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    st.write(f"Dataset: Iris ({df.shape[0]} samples, {df.shape[1]} features)")
    st.write(df.head())
elif sample_data == "Wine":
    from sklearn.datasets import load_wine
    data = load_wine()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    st.write(f"Dataset: Wine ({df.shape[0]} samples, {df.shape[1]} features)")
    st.write(df.head())
elif sample_data == "Digits":
    from sklearn.datasets import load_digits
    data = load_digits()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    st.write(f"Dataset: Digits ({df.shape[0]} samples, {df.shape[1]} features)")
    st.write(df.head())
else:
    st.warning("Please upload a dataset or select one from the dropdown.")

# Select number of clusters for K-Means and Agglomerative
num_clusters = st.sidebar.slider("Select Number of Clusters", min_value=2, max_value=10, value=3)

# Choose clustering model
clustering_model = st.sidebar.selectbox("Select Clustering Algorithm", ["K-Means", "DBSCAN", "Agglomerative Clustering"])

# DBSCAN Epsilon slider
epsilon =  st.sidebar.slider("Select DBSCAN Epsilon", min_value=0.1, max_value=2.0, value=0.5, step=0.1)

# Standardizing the data
scaler = StandardScaler()
scaled_df = scaler.fit_transform(df)

# Apply the chosen clustering model
if clustering_model == "K-Means":
    with st.expander("K-Means Clustering"):
        st.write("""
        **K-Means** is a distance-based clustering algorithm that partitions the dataset into a predefined number of clusters (`n_clusters`).
        The algorithm minimizes the within-cluster sum of squares (WCSS), ensuring that the data points in each cluster are as close as possible to their respective centroids.
        """)
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(scaled_df)
    df['Cluster'] = kmeans.labels_
    model = kmeans
    performance_score = silhouette_score(scaled_df, kmeans.labels_)
    st.write(f"Silhouette Score for K-Means: {performance_score:.2f}")

elif clustering_model == "DBSCAN":
    with st.expander("DBSCAN Clustering"):
        st.write("""
        **DBSCAN** (Density-Based Spatial Clustering of Applications with Noise) is a clustering algorithm that identifies clusters based on the density of points.
        It is particularly effective for datasets with noise, as it can automatically identify outliers (points that don't belong to any cluster).
        The `eps` parameter controls the density threshold, and `min_samples` sets the minimum number of points required to form a cluster.
        """)
    dbscan = DBSCAN(eps=epsilon, min_samples=5)
    dbscan.fit(scaled_df)
    df['Cluster'] = dbscan.labels_
    model = dbscan
    performance_score = silhouette_score(scaled_df, dbscan.labels_) if len(set(dbscan.labels_)) > 1 else -1
    st.write(f"Silhouette Score for DBSCAN: {performance_score:.2f}")

elif clustering_model == "Agglomerative Clustering":
    with st.expander("Agglomerative Clustering Explanation"):
        st.write("""
        **Agglomerative Clustering** is a hierarchical clustering method that builds a tree of clusters from bottom to top. 
        It merges pairs of clusters that are closest together at each step, based on a similarity metric.
        You can control the number of clusters by setting `n_clusters`. It is useful when you want to observe how data can be clustered at different levels of granularity.
        """)
    agglomerative = AgglomerativeClustering(n_clusters=num_clusters)
    agglomerative.fit(scaled_df)
    df['Cluster'] = agglomerative.labels_
    model = agglomerative
    performance_score = silhouette_score(scaled_df, agglomerative.labels_)
    st.write(f"Silhouette Score for Agglomerative Clustering: {performance_score:.2f}")

# PCA for 2D visualization
pca = PCA(n_components=2)
pca_result = pca.fit_transform(scaled_df)
df['PCA1'] = pca_result[:, 0]
df['PCA2'] = pca_result[:, 1]

# t-SNE for better visualization
tsne = TSNE(n_components=2, random_state=42)
tsne_result = tsne.fit_transform(scaled_df)
df['TSNE1'] = tsne_result[:, 0]
df['TSNE2'] = tsne_result[:, 1]

# Display Elbow Plot for KMeans
if clustering_model == "K-Means":
    with st.expander("Elbow Plot (K-Means) Explanation"):
        st.write("""
        The **Elbow Plot** is used to determine the optimal number of clusters for **K-Means**. 
        It plots the **within-cluster sum of squares (WCSS)** against the number of clusters. The "elbow" point on the plot suggests the optimal number of clusters, 
        as adding more clusters beyond this point does not significantly reduce the WCSS.
        """)
    wcss = []
    for i in range(1, 11):
        kmeans_temp = KMeans(n_clusters=i, random_state=42)
        kmeans_temp.fit(scaled_df)
        wcss.append(kmeans_temp.inertia_)
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, 11), wcss)
    plt.title('Elbow Method')
    plt.xlabel('Number of Clusters')
    plt.ylabel('WCSS')
    st.pyplot(plt)

# Performance Metrics
with st.expander("Performance Metrics"):
    st.subheader("Performance Metrics Comparison")
    db_score = davies_bouldin_score(scaled_df, model.labels_)
    st.write(f"Davies-Bouldin Index: {db_score:.2f}; The DBI calculates the average similarity of each cluster to its most similar neighbor, with lower values indicating better separation. A lower DBI suggests that the clusters are more distinct and not overlapping, which is ideal for clustering models.")

# Visualizations
with st.expander("Clustering Visualizations"):
    st.subheader("Clustering Visualization (PCA)")
    fig = px.scatter(df, x='PCA1', y='PCA2', color='Cluster', title=f"{clustering_model} Clustering (PCA)")
    st.plotly_chart(fig)

st.subheader("t-SNE Clustering Visualization")
fig_tsne = px.scatter(df, x='TSNE1', y='TSNE2', color='Cluster', title=f"{clustering_model} Clustering (t-SNE)")
st.plotly_chart(fig_tsne)

# Option to export the results
with st.expander("Export Results"):
    st.subheader("Export Results")
    export_csv = df.to_csv(index=False)
    st.download_button(
        label="Download Clustering Results (CSV)",
        data=export_csv,
        file_name="clustering_results.csv",
        mime="text/csv",
    )

st.write("""
You can compare the clustering performance of different models, experiment with parameters, and visualize the results interactively.
""")
