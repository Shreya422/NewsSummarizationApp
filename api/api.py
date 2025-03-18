from fastapi import FastAPI
from api.news_extractor import get_news_urls, extract_news_content
from api.sentiment_analysis import analyze_sentiment
from api.comparitive_analysis import comparative_sentiment_analysis
from api.text_to_speech import generate_hindi_speech

app = FastAPI()

@app.get("/news/")
def fetch_news(company_name: str):
    urls = get_news_urls(company_name)
    articles = [extract_news_content(url) for url in urls if extract_news_content(url)]
    
    for article in articles:
        article["sentiment"] = analyze_sentiment(article["summary"])
    
    comparison = comparative_sentiment_analysis(articles)
    
    summary_text = " ".join([article["summary"] for article in articles])
    audio_file = generate_hindi_speech(summary_text)
    
    return {
        "company": company_name,
        "articles": articles,
        "comparative_analysis": comparison,
        "audio_file": audio_file
    }
