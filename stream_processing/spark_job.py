from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, LongType, IntegerType
from pyspark.sql.streaming import StreamingQueryException

schema = StructType([
    StructField("timestamp", LongType(), True),
    StructField("value", IntegerType(), True)
])

spark = SparkSession.builder \
    .appName("RealTimeProcessing") \
    .getOrCreate()

df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "data_topic") \
    .load()

json_df = df.selectExpr("CAST(value AS STRING) as json")
data_df = json_df.select(from_json(col("json"), schema).alias("data")).select("data.*")

# Write to console for debugging
query = data_df \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

try:
    query.awaitTermination()
except StreamingQueryException:
    query.stop()
