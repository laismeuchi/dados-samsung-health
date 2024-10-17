# Databricks notebook source
from pyspark.sql import Row

data = [ 
        Row(id=1001, activity='Walking'),
        Row(id=1002, activity='Running'),
        Row(id=11007, activity='Bike'),
        Row(id=14001, activity='Pool Swim'),
        Row(id=15005, activity='Treadmill')
        ]
df = spark.createDataFrame(data)

# COMMAND ----------

display(df)

# COMMAND ----------

df.write.format("delta") \
    .option("mergeSchema", "true") \
    .mode("overwrite") \
    .saveAsTable("g_exercise_type")
