from kafka import KafkaProducer
import json
import requests
import time
import logging

# Kafka Configuration
kafka_broker = 'localhost:9092'
kafka_topic = 'news_topic'

# NewsAPI Configuration
api_key = '6fbd22bbbb8346b8891950adebb1fd72' # Get your API Key from https://newsapi.org/
keywords = ['Politics', 'Health', 'AI'] # You can change these keywords according to your requirements
sources = 'bbc-news,cnn,fox-news,nbc-news,the-guardian-uk,the-new-york-times,the-washington-post,usa-today,independent,daily-mail'
newsapi_endpoint = 'https://newsapi.org/v2/everything'

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers=kafka_broker,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def fetch_news():
    for keyword in keywords:
        params = {
            'q': keyword,
            'apiKey': api_key,
            'sources': sources,
            'pageSize': 10  # You can adjust this
        }
        response = requests.get(newsapi_endpoint, params=params)
        if response.status_code == 200:
            articles = response.json().get('articles', [])
            for article in articles:
                article_title = article.get('title', 'No Title')
                if not article_title.strip():  # Check if title is empty or whitespace
                    article_title = "No Title"
                    logger.warning(f"Empty title or [Removed] in article from source: {article.get('source', 'Unknown')}")
                logger.info(f"Fetching article: {article_title}")
                print(f"Fetching article: {article_title}")  # Print article title
                producer.send(kafka_topic, article)
                time.sleep(1)  # To avoid rate limit
        else:
            logger.error("Error fetching news:", response.text)

if __name__ == '__main__':
    while True:
        fetch_news()
        time.sleep(60)  # Fetch news every 1 minute