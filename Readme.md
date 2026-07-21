# Real-Time News Named Entity Recognition Pipeline

A real-time data streaming pipeline that collects live news articles, extracts named entities using spaCy, and visualizes trending entities with Elasticsearch and Kibana.

## Project Overview

This project demonstrates how to build a real-time data processing pipeline using Apache Kafka, Apache Spark Structured Streaming, spaCy, Elasticsearch, and Kibana. News articles are continuously fetched from NewsAPI, streamed through Kafka, processed with Spark, analyzed using Named Entity Recognition (NER), and finally stored in Elasticsearch for visualization in Kibana.

## Technologies Used

- Python
- Apache Kafka
- Apache Spark Structured Streaming
- spaCy
- Elasticsearch
- Kibana
- Logstash
- NewsAPI

## Pipeline

NewsAPI → Python Producer → Kafka → Spark Structured Streaming → spaCy Named Entity Recognition → Logstash → Elasticsearch → Kibana Dashboard

## Results

The visualization results generated in Kibana can be found in
`Visualization_Report.pdf`.

## How to Run

### 1. Start Apache Kafka

Start the Kafka broker.

### 2. Start Elasticsearch

Launch Elasticsearch.

### 3. Start Logstash

Run Logstash using the provided configuration file.

### 4. Start Kibana

Launch Kibana to visualize the indexed entities.

### 5. Run the Producer

```bash
python producer.py
```

### 6. Run the Spark Consumer

```bash
spark-submit consumer.py
```
