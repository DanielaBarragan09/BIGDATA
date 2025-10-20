from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, LongType

# Crear sesión Spark
spark = SparkSession.builder \
    .appName("KafkaSparkStreaming") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Conectarse al topic de Kafka
df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "sensores") \
    .load()

# Definir el esquema del JSON
schema = StructType([
    StructField("sensor_id", StringType()),
    StructField("temperature", DoubleType()),
    StructField("humidity", DoubleType()),
    StructField("timestamp", LongType())
])

# Extraer datos del JSON
data = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

# Mostrar los datos en consola en tiempo real
query = data.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
