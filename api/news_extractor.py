import requests
from bs4 import BeautifulSoup
from newspaper import Article
import random

def get_news_urls(company_name):
    """
    Fetches URLs of news articles related to the given company.
    """
    query = f"{company_name} news"
    search_url = f"https://www.google.com/search?q={query}&tbm=nws"
    headers = {"User-Agent": "Chrome/134.0.0.0"}
    # Mozilla/5.0
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    urls = []
    for link in soup.select("a[href^='/url?q=']"):
        url = link['href'].split("?q=")[1].split("&")[0]
        if "https://" in url and "google" not in url:
            urls.append(url)
    
    return list(set(urls))[:10]  # Limit to 10 unique articles

def extract_news_content(url):
    """
    Extracts title, summary, and content from a news article.
    """
    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        return {
            "title": article.title,
            "summary": article.summary,
            "content": article.text
        }
    except:
        return None
