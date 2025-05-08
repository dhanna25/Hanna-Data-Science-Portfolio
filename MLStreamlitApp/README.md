## Project Overview
This project is an interactive machine learning web app built using Streamlit that allows users to explore the fundamentals of supervised learning through logistic regression. The primary goal of the app is to create an educational and user-friendly environment where users can upload their own datasets or choose from a selection of preloaded ones, define a target variable, and instantly build and evaluate a logistic regression model. The app handles preprocessing automatically, making it easy to work with both numeric and categorical data. Users can interactively adjust the test-train split ratio and regularization strength (C) to observe how these hyperparameters affect model performance. Key evaluation metrics such as accuracy, precision, and recall are displayed, along with a detailed classification report. For binary classification problems, the app also generates a Receiver Operating Characteristic (ROC) curve and calculates the Area Under the Curve (AUC) score. 

## Intructions
1. Install the required dependencies using pip install requirements.txt. 

2. Once drpendencies are installed, the app can be launched with streamlit run /Users/dinahanna/Documents/GitHub/Hanna-Data-Science-Portfolio/MLStreamlitApp/mlstreamlit.py

3. The app will be accessible in the browser at localhost:8501

4. Deployed Version:  You can access the deployed version using the link provided: https://dhanna25-hanna-data-science-po-mlstreamlitappmlstreamlit-lpmb5d.streamlit.app/

## App Features 

### Models Used: 
- **Logistic Regression**: Primary model in the app. It is a binary classifier but can be used for multiclass classification tasks as well (with the OvR strategy).
- The app allows hyperparameter tuning, such as adjusting the regularization strength (C) and the test/train split ratio.

### How Hyperparameters Are Selected/Tuned:
- **Test Size**: The user can adjust the proportion of data to be used for testing the model. This affects how the model is trained and evaluated.
- **Regularization Strength (C)**: The user can change the value of C, which controls the regularization. Higher values of C reduce regularization, while smaller values of C increase regularization, helping to prevent overfitting.

### References
- **[Streamlit](https://docs.streamlit.io/)**
- **[Scikit-learn Documentation](https://scikit-learn.org/stable/)**
- **[Logistic Regression Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)**
- **[Confusion Matrix and AUC Calculation](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics)**

### Visual Examples
<img width="500" alt="Screenshot 2025-04-14 at 5 46 25 PM" src="https://github.com/user-attachments/assets/ccd764b0-77f4-4981-8277-c5129598b583" />
<img width="500" alt="Screenshot 2025-04-14 at 5 47 59 PM" src="https://github.com/user-attachments/assets/b5952356-0322-4922-bcbb-f0cfb2a45989" />
<img width="680" alt="Screenshot 2025-04-14 at 5 51 36 PM" src="https://github.com/user-attachments/assets/33830bdf-143b-486f-b46e-e22ec5ccc340" />
