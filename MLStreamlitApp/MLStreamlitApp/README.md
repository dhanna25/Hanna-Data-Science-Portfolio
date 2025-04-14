# MLStreamlitApp
 This project is an interactive machine learning web application built with Streamlit, designed to help users explore supervised classification models. Its primary goal is to make machine learning concepts more approachable by allowing users to train, evaluate, and visualize models. Users can upload their own CSV files or choose from well-known sample datasets like Iris, Breast Cancer, Wine, Digits, and others. After selecting a dataset, users define the target variable, tweak model hyperparameters, and view evaluation metrics including accuracy, precision, recall, and AUC. The app also provides visual outputs like confusion matrix heatmaps, making it a valuable learning tool for students, educators, and early-career data scientists.

To run the app locally, clone the repository and install the dependencies listed in requirements.txt. Once your environment is set up, launch the app with streamlit run /Users/dinahanna/Documents/GitHub/Hanna-Data-Science-Portfolio/MLStreamlitApp/MLStreamlitApp/ml.py. The project relies on key libraries such as streamlit>=1.25, pandas>=1.5, numpy>=1.22, scikit-learn>=1.2, seaborn>=0.12, and matplotlib>=3.6. A live, deployed version is also available on Streamlit Cloud, providing instant access without any setup.

The app currently supports three supervised learning algorithms: Logistic Regression, Decision Tree Classifier, and K-Nearest Neighbors. Each model includes adjustable hyperparameters accessible via the sidebar. Users can control parameters like regularization strength (C) for Logistic Regression, allowing for hands-on experimentation and an understanding of how these values affect performance.

This project was developed with guidance from official documentation and tutorials, including the Scikit-learn and Streamlit documentation, as well as the Streamlit blog. These resources were key in shaping the structure of the app, especially in implementing training workflows, metric evaluations, and interactive visualizations.

Included in the app are examples of generated visualizations such as dataset previews, confusion matrices, and ROC curves. These outputs help users better understand model performance and make thoughtful decisions about tuning and feature select
 
 

