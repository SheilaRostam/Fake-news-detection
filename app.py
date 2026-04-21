import streamlit as st
import joblib

vectorizer = joblib.load(r"C:\Users\Espen\PycharmProjects\PythonProject\vectorizer.jb")
model = joblib.load(r"C:\Users\Espen\PycharmProjects\PythonProject\lr_model.jb")

st.title("fake news detector")
st.write("enter a news article below to check whether its true or fake")

news_input = st.text_input("News article: ")

if st.button ("check news"):
    if news_input.strip():
        transform_input = vectorizer.transform([news_input])
        prediction = model.predict(transform_input)

        if prediction == 1:
            st.error("The news is fake news")
        if prediction == 0:
            st.success("The news is real news")

    else:
        st.warning("Please enter some text to analyze")