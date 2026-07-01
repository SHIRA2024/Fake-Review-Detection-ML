import streamlit as st
import joblib

model = joblib.load("models/best_fake_review_model.pkl")

st.title("Fake Review Detection")

st.write(
    "Enter a product review and the model will predict whether it is likely real or fake."
)

review = st.text_area("Review", height=160)

if st.button("Analyze"):
    if review.strip() == "":
        st.warning("Please enter a review.")
    else:
        prediction = model.predict([review])[0]

        probabilities = model.predict_proba([review])[0]
        classes = model.classes_
        confidence = probabilities[list(classes).index(prediction)] * 100

        if prediction == "Fake":
            st.error(f"Prediction: Fake Review\n\nConfidence: {confidence:.2f}%")
        else:
            st.success(f"Prediction: Real Review\n\nConfidence: {confidence:.2f}%")