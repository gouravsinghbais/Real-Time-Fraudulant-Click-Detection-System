#!/usr/bin/env python3

import time
import json

from kafka import KafkaProducer


def get_click_count():
    file = open('/Users/userabc/click_count.json')
    click_data = json.load(file)

    return click_data['click_count']

def get_json_data():
    data = {}

    data["click_count"] = get_click_count()

    return json.dumps(data) 

def main():
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10, 1))

    json_data = get_json_data()
    print(json_data)
    kafka_topic = 'fcd-producer'
    kafka_topic = kafka_topic.encode(encoding = 'UTF-8')
    producer.send(kafka_topic, bytes(f'{json_data}','UTF-8'))
    print(f"Ad click data is sent: {json_data}")
    time.sleep(5)


if __name__ == "__main__":
    main()