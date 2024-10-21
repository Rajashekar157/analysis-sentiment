import streamlit as st

def analyze_sentiment(text):
    # Dummy sentiment analysis
    if "good" in text or "happy" in text:
        return "Positive"
    elif "bad" in text or "sad" in text:
        return "Negative"
    else:
        return "Neutral"

st.title("Sentiment Analysis App")
st.write("Enter a sentence to analyze its sentiment.")

# Text input
user_input = st.text_area("Type your text here:")

if user_input:
    # Get sentiment analysis result
    sentiment = analyze_sentiment(user_input)
    
    # Display the result
    st.write(f"Sentiment: **{sentiment}**")


