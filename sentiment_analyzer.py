import re
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import json 

def clean_text(text):
    if text!=text:
        return text
    text = re.sub('<a.*/a>', '', text)
    text = re.sub('https{0,1}.*', '', text)
    text = re.sub('@[a-zA-Z0-9_]+', '', text)
    text = re.sub('#[a-zA-Z0-9_]+', '', text)
    text = ''.join([i for i in text if i.isalnum() or i.isspace()])
    return text.strip()

def stopword(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_sentence = " ".join([w for w in word_tokens if not w.lower() in stop_words])
    return filtered_sentence




def sentiment(text):
    with open('sentiments.json','r') as r:
        sentiments_json = json.load(r)
    sia = SentimentIntensityAnalyzer()
    sia.lexicon.update(sentiments_json)
    sentiment_dict = sia.polarity_scores(text)
    sentiment_str = ""
    if sentiment_dict['compound'] >= 0.05 :
        sentiment_str =  "Positive"
 
    elif sentiment_dict['compound'] <= - 0.05 :
        sentiment_str =  "Negative"
 
    else :
        sentiment_str =  "Neutral"

    return sentiment_dict['compound'], sentiment_str




def get_sentiment(text):
    text = clean_text(text)
    filtered = stopword(text)
    return sentiment(filtered)