from collections import Counter

def comparative_sentiment_analysis(articles):
    """
    Aggregates sentiment results across articles and identifies trends.
    """
    sentiment_counts = Counter([article["sentiment"] for article in articles])
    total_articles = len(articles)

    sentiment_distribution = {k: round(v / total_articles, 2) for k, v in sentiment_counts.items()}
    common_topics = list(set(topic for article in articles for topic in article["summary"].split()))

    return {
        "sentiment_distribution": sentiment_distribution,
        "common_topics": common_topics
    }
