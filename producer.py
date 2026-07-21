import time
from kafka import KafkaProducer
from newsapi import NewsApiClient

# Kafka configuration
kafka_bootstrap_servers = "localhost:9092"  # Replace with your Kafka bootstrap servers
kafka_topic = "api-topic"  # Replace with your Kafka input topic

# News API configuration
news_api_key = "YOUR_API_KEY"  # Replace with your News API key
newsapi = NewsApiClient(api_key=news_api_key)

# Create Kafka producer
producer = KafkaProducer(
    bootstrap_servers=kafka_bootstrap_servers,
    value_serializer=lambda v: str(v).encode('utf-8')
)

def fetch_and_push_news():
    try:
        # Fetch top headlines from News API
        news = newsapi.get_top_headlines(country='us', category='business', language='en')

        # Push each article to Kafka
        for article in news['articles']:
            if (article['content']):
                producer.send(kafka_topic, value=article['content'])

        print("News pushed to Kafka")

    except Exception as e:
        print(f"Error: {str(e)}")

# Schedule the job to run every 10 seconds
while True:
    fetch_and_push_news()
    time.sleep(900)
