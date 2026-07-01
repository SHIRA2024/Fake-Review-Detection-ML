# GPT Work Log

This file documents how ChatGPT was used during the development of the project.

---

## Project Selection

**Prompt**

"I am looking for a machine learning project with an existing dataset."

**Outcome**

After comparing several ideas (phishing detection, movie recommendation, fraud detection), we selected **Fake Review Detection** because:

- Public dataset available
- Binary classification problem
- Relevant real-world application
- Fits the course requirements

---

## Dataset Exploration (EDA)

**Prompt**

"Help me analyze the dataset before building a model."

**Outcome**

- Checked dataset structure
- Verified labels (CG = Fake, OR = Real)
- Analyzed review length
- Analyzed word count
- Visualized class distribution
- Created Word Clouds

---

## Baseline Model

**Prompt**

"Build a baseline model for fake review detection."

**Outcome**

- TF-IDF Vectorizer
- Multinomial Naive Bayes
- Accuracy: ~84%

---

## Logistic Regression

**Prompt**

"Improve the baseline model."

**Outcome**

- Trained Logistic Regression
- Evaluated using Accuracy and Classification Report
- Improved performance over Naive Bayes

---

## Linear SVM

**Prompt**

"Try a Support Vector Machine classifier."

**Outcome**

- Replaced Logistic Regression with Linear SVM
- Compared performance
- Improved overall accuracy

---

## Feature Engineering

**Prompt**

"Improve the model using better text features."

**Outcome**

- Added TF-IDF Bigrams
- Compared performance with the baseline
- Achieved approximately 90% accuracy

---

## Hyperparameter Tuning

**Prompt**

"Optimize the SVM using GridSearchCV."

**Outcome**

Optimized:

- C
- min_df
- ngram_range

Selected the best performing model using cross-validation.

---

## Model Calibration

**Prompt**

"Allow the model to return prediction confidence."

**Outcome**

- Wrapped the classifier with CalibratedClassifierCV
- Added confidence score prediction
- Saved the final model using Joblib

---

## Streamlit Application

**Prompt**

"Create a simple web interface for the trained model."

**Outcome**

Built a Streamlit application that allows users to:

- Enter a review
- Predict whether it is Fake or Real
- Display the model confidence

---

## Model Comparison

**Prompt**

"Compare all trained models."

**Outcome**

Compared:

- Multinomial Naive Bayes
- Logistic Regression
- Linear SVM
- Linear SVM + Bigrams
- Linear SVM + GridSearch
- Final Calibrated SVM

Created:

- Performance table
- Accuracy comparison chart

---

## Documentation

**Prompt**

"Help prepare the project for submission."

**Outcome**

Generated:

- README
- Requirements file
- Streamlit screenshots
- Model comparison figure
- GPT work log
