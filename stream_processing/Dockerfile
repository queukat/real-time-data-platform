FROM bitnami/spark:3.0.1

COPY spark_job.py /opt/bitnami/spark/

CMD ["/opt/bitnami/spark/bin/spark-submit", "/opt/bitnami/spark/spark_job.py"]
