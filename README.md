# Power Monitor System

## Description

The system is designed to achieve real-time collection of electricity consumption data from various appliances. It utilizes several key services for streaming, database management, and monitoring:

- Streaming: Kafka
- NoSQL Database: ElasticSearch
- Monitoring: Grafana, Prometheus, kafka-exporter, elasticsearch-exporter

## Requirements
- Docker
- Python

# Setup
1. Configuring the Environment
    
    - Navigate to the `power_producer`
    
    - Setting Environment Variables
    
      Create `.env` file in the current folder

      ```.env
      KAFKA_SERVER='kafka:9092'
      TOPIC_NAME='smart_meter_data'
      ```

2. Setting up Docker Services

    - Navigate to the `docker_services`

    - Starting Docker Services

      ```shell
      docker-compose up -d
      ```

    - Checking Docker Container Status
      After starting the Docker services, verify the status of the containers.
      
      ```shell
      docker-compose ps
      ```

3. Monitoring the Service Performance