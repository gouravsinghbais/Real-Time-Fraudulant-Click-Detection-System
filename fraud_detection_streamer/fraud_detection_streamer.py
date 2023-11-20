from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *


spark = SparkSession\
    .builder\
    .appName("Fraud Click Detection")\
    .getOrCreate()


df = spark\
    .readStream\
    .format("kafka")\
    .option("kafka.bootstrap.servers", "localhost:9092")\
    .option("subscribe", "fcd-producer")\
    .load()

jsonschema = StructType([StructField("click_count", IntegerType())])

df = df\
    .select(from_json(col("value").cast(StringType()), jsonschema).alias("value"))\
    .select("value.*")\
    .withColumn('fraudClick', when(col('click_count') > 3, "Yes").otherwise("No"))\
    .withColumn("value", to_json(struct(col("fraudClick"))))

query = df\
    .writeStream\
    .format('kafka')\
    .option('kafka.bootstrap.servers', 'localhost:9092')\
    .option('topic', 'fcd-consumer')\
    .option('checkpointLocation', '/Users/userabc/chkpoint')\
    .start()


query.awaitTermination()