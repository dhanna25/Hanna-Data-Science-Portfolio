import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
   accuracy_score, precision_score, recall_score, roc_auc_score,
   confusion_matrix, roc_curve, classification_report
)
from sklearn.preprocessing import LabelEncoder, StandardScaler, label_binarize
from sklearn.datasets import (
   load_breast_cancer, load_iris, load_wine, load_digits,
   load_diabetes, fetch_covtype, load_linnerud
)


# Configuring the Streamlit page layout and title
st.set_page_config(page_title="ML Playground", layout="wide")
st.title("Supervised ML Playground with Logistic Regression")


# Sidebar allows the user to upload a custom dataset or select a sample dataset
st.sidebar.header("1. Upload or Choose Dataset")
uploaded_file = st.sidebar.file_uploader("📁 Upload CSV", type=["csv"])

#Options for selecting a sample dataset
sample_dataset = st.sidebar.selectbox(
   "📚 Or use a sample dataset",
   options=[
       "None",
       "Breast Cancer",
       "Iris",
       "Wine",
       "Digits",
       "Diabetes",
       "Covertype (small preview)",
       "Linnerud"
   ]
)

# Dataset descriptions with a brief explanation of each dataset
dataset_descriptions = {
   "Breast Cancer": "🔬 Binary classification to detect malignant vs benign tumors.",
   "Iris": "🌸 Multiclass classification for flower species.",
   "Wine": "🍷 Multiclass classification of wine cultivars by chemistry.",
   "Digits": "✍️ Handwritten digit classification (0–9).",
   "Diabetes": "🩺 Regression task for disease progression (not ideal for logistic regression).",
   "Covertype (small preview)": "🌲 Forest cover type classification from cartographic features.",
   "Linnerud": "🏃 Multi-output regression on physiological data."
}

# Function to load sample datasets based on user selection
def load_sample_dataset(name):
   if name == "Breast Cancer":
       return load_breast_cancer(as_frame=True).frame
   elif name == "Iris":
       return load_iris(as_frame=True).frame
   elif name == "Wine":
       return load_wine(as_frame=True).frame
   elif name == "Digits":
       return load_digits(as_frame=True).frame
   elif name == "Diabetes":
       return load_diabetes(as_frame=True).frame
   elif name == "Covertype (small preview)":
       data = fetch_covtype(as_frame=True)
       return data.frame.sample(1000, random_state=42)
   elif name == "Linnerud":
       return load_linnerud(as_frame=True).frame
   else:
       return None

# Load dataset based on user input: uploaded file or sample dataset
if uploaded_file:
   df = pd.read_csv(uploaded_file)
   st.info("✅ Custom dataset uploaded.")
elif sample_dataset != "None":
   df = load_sample_dataset(sample_dataset)
   st.info(f"✅ Loaded sample dataset: **{sample_dataset}**")
   if sample_dataset in dataset_descriptions:
       st.markdown(f"> {dataset_descriptions[sample_dataset]}")
else:
   st.warning("Please upload a dataset or select a sample dataset.")
   st.stop()


# Displaying a preview of the loaded dataset
st.subheader("📄 Dataset Preview")
st.dataframe(df.head(), use_container_width=True)


# Sidebar for selecting the target column for model prediction
st.sidebar.header("2. Select Target Column")
target_column = st.sidebar.selectbox("🎯 Target Column", df.columns)


# Encoding the target column if it is categorical (non-numeric)
if df[target_column].dtype == 'object':
   df[target_column] = LabelEncoder().fit_transform(df[target_column])

X = df.drop(columns=[target_column])
y = df[target_column]

# Re-encode target in case it was transformed
y = LabelEncoder().fit_transform(y)

# One-hot encode categorical features for the model
X = pd.get_dummies(X)

# Feature scaling to standardize dsta
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# Sidebar for adjusting model settings like test size and regularization strength (C)
st.sidebar.header("3. Adjust Model Settings")
test_size = st.sidebar.slider("🧪 Test Set Size", 0.1, 0.5, 0.3)
C = st.sidebar.slider("📉 Regularization Strength (C)", 0.01, 10.0, 1.0)

# Splitting the dataset into training and test sets based on the selected test size
X_train, X_test, y_train, y_test = train_test_split(
   X_scaled, y, test_size=test_size, random_state=42
)

# Initializing and training the logistic regression model
model = LogisticRegression(C=C, max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)

# Displaying performance metrics like accuracy, precision, and recall
st.subheader("📈 Model Performance Overview")
col1, col2, col3 = st.columns(3)
col1.metric("🎯 Accuracy", f"{accuracy_score(y_test, y_pred):.2f}")
col2.metric("⚖️ Precision", f"{precision_score(y_test, y_pred, average='weighted'):.2f}")
col3.metric("📣 Recall", f"{recall_score(y_test, y_pred, average='weighted'):.2f}")


with st.expander("🧾 View Detailed Classification Report"):
   st.text(classification_report(y_test, y_pred))

# Visualizing confusion matrix using seaborn heatmap
st.subheader("📊 Confusion Matrix")
fig, ax = plt.subplots()
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt="d", cmap="YlGnBu", ax=ax)
ax.set_xlabel("Predicted")
ax.set_ylabel("Actual")
st.pyplot(fig)

# If binary classification, display ROC curve and AUC score
if len(np.unique(y)) == 2:
   st.subheader("📉 ROC Curve & AUC Score")
   auc = roc_auc_score(y_test, y_prob[:, 1])
   st.metric("📊 AUC Score", f"{auc:.2f}")


   fpr, tpr, _ = roc_curve(y_test, y_prob[:, 1])
   fig2, ax2 = plt.subplots()
   ax2.plot(fpr, tpr, label="ROC Curve", linewidth=2)
   ax2.plot([0, 1], [0, 1], linestyle='--', color='gray')
   ax2.set_xlabel("False Positive Rate")
   ax2.set_ylabel("True Positive Rate")
   ax2.set_title("ROC Curve")
   ax2.legend()
   st.pyplot(fig2)
else:
   st.subheader("📈 Multiclass AUC Score")
   class_labels = np.unique(y)
   y_test_binarized = label_binarize(y_test, classes=class_labels)

 # Check for consistency in class labels for multiclass AUC
   if y_prob.shape[1] != y_test_binarized.shape[1]:
       st.warning("⚠️ AUC not calculated: mismatch between class labels and prediction probabilities.")
   else:
       try:
           auc = roc_auc_score(y_test_binarized, y_prob, multi_class='ovr')
           st.metric("📊 Multiclass AUC (OvR)", f"{auc:.2f}")
           st.info("🚧 Multiclass ROC curve visualization is not supported in this app yet.")
       except Exception as e:
           st.error(f"Error calculating AUC: {e}")