# Proyecto: Procesamiento de Datos con Apache Spark y Kafka

## 🧩 Descripción General

Este proyecto implementa un flujo de procesamiento **batch y en tiempo real** utilizando **Apache Spark** y **Apache Kafka**.  
El sistema simula datos de sensores (temperatura y humedad) que se envían a Kafka y luego se procesan con Spark Streaming para su análisis en tiempo real.

---

## ⚙️ Requisitos Previos

- **Apache Kafka** instalado y configurado.
- **Apache Spark** con soporte para Structured Streaming.
- **Python 3.8 o superior.**

Instalar dependencias con:
```bash
pip install -r requirements.txt

sudo /opt/Kafka/bin/zookeeper-server-start.sh /opt/Kafka/config/zookeeper.properties &
sudo /opt/Kafka/bin/kafka-server-start.sh /opt/Kafka/config/server.properties &

/opt/Kafka/bin/kafka-topics.sh --create --topic sensores --bootstrap-server localhost:9092
python3 data_generator.py
{"sensor_id": 3, "temperature": 28.45, "humidity": 51.22, "timestamp": 1760757984}
spark-submit streaming_processing.py

http://localhost:4040
spark-submit batch_processing.py
