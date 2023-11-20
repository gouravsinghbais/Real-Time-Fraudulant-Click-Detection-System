FROM python:3.11
USER root
RUN pip install kafka-python
ADD fraud_detection_producer.py /Users/userabc/
ADD click_count.json /Users/userabc/
RUN chmod a+x /Users/userabc/fraud_detection_producer.py
ENTRYPOINT ["/Users/userabc/fraud_detection_producer.py"]