# Big-Data-con-Hadoop-MapReduce
# Proyecto MapReduce WordCount en Hadoop Streaming

## ¿Qué hace?

Este proyecto implementa un trabajo MapReduce utilizando Hadoop Streaming y scripts en Python para realizar un conteo de palabras (WordCount) sobre un conjunto de archivos de texto. La solución está diseñada para ejecutarse en un entorno Hadoop configurado localmente (Docker o pseudo-distribuido) y permite analizar el rendimiento variando el número de reducers.

---

## ¿Cómo ejecutarlo?

### 1. Cargar archivos a HDFS:

```bash
hdfs dfs -mkdir -p /user/root/input
hdfs dfs -put data1.txt /user/root/input/
hdfs dfs -put data2.txt /user/root/input/


## Ejecutar job MapReduce con 1 reducer
hdfs dfs -rm -r /user/root/output1

hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -D mapreduce.job.reduces=1 \
  -input /user/root/input \
  -output /user/root/output1 \
  -mapper /root/mapper.py \
  -reducer /root/reducer.py

##Ver resultados:

hdfs dfs -cat /user/root/output1/part-00000

Starlyn Mateo
23-0977
