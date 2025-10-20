from pyspark.sql import SparkSession

# Crear sesión Spark
spark = SparkSession.builder.appName("BatchProcessingExample").getOrCreate()

# Cargar datos CSV
df = spark.read.csv("data/sensores.csv", header=True, inferSchema=True)

# Limpiar y analizar
df_clean = df.dropna()
df_clean.groupBy("sensor_id").avg("temperature", "humidity").show()

# Guardar resultados
df_clean.write.csv("results/avg_results.csv", header=True)
