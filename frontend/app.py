import streamlit as st
import requests

st.title("News Summarization and Sentiment Analysis")
company_name = st.text_input("Enter Company Name")

if st.button("Fetch News"):
    response = requests.get(f"http://127.0.0.1:8000/news/?company_name={company_name}")
    if response.status_code == 200:
        data = response.json()
        
        st.write(f"### News Summaries for {company_name}")
        for article in data["articles"]:
            st.write(f"**Title:** {article['title']}")
            st.write(f"**Summary:** {article['summary']}")
            st.write(f"**Sentiment:** {article['sentiment']}")
            st.write("---")
        
        st.write("### Comparative Sentiment Analysis")
        st.json(data["comparative_analysis"])
        
        st.audio(data["audio_file"])
    else:
        st.error("Failed to fetch news.")
