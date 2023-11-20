FROM python:3.11
USER root
RUN apk update && apk add bash && apk add openjdk11
RUN pip install pyspark
ADD fraud_detection_streamer.py /Users/userabc
RUN wget https://dlcdn.apache.org/spark/spark-3.3.0/spark-3.3.0-bin-hadoop3.tgz -P /Users/userabc
RUN cd /Users/userabc && tar -xzvf /Users/userabc/spark-3.3.0-bin-hadoop3.tgz
RUN chmod a+x /Users/userabc/spark-3.3.0-bin-hadoop3/bin/spark-submit
ENTRYPOINT ["/Users/userabc/spark-3.3.0-bin-hadoop3/bin/spark-submit","--packages","org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0","/Users/userabc/fraud_detection_streamer.py"]