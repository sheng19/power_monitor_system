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

# Service Performance
   - Kafka Performance
     <img width="1600" alt="image" src="https://github.com/sheng19/power_monitor_system/assets/49142310/a7248c09-2131-4d24-ba44-33d346fd1eb0">

   - ElasticSearch Performance
     ![image](https://github.com/sheng19/power_monitor_system/assets/49142310/714cf9dc-487d-4f23-ae71-0e46de22352a)
