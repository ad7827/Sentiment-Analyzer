import streamlit as st
from sentiment_analyzer import get_sentiment

text = st.text_area('Enter Tweet')

button = st.button("Submit")

if text and button:
    sentiment_score, sentiment_str = get_sentiment(text)
    st.write('Sentiment score: ', str(sentiment_score))
    st.write('The sentence is ',sentiment_str)