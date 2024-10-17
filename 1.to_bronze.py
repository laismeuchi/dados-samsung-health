# Databricks notebook source
df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("skipRows", 1) \
    .load("/mnt/stshealthreader/attachments/shealth")

# COMMAND ----------

# remove prefix on the column name
new_column_names = [col.replace('com.samsung.health.exercise.', '') for col in df.columns]
df = df.toDF(*new_column_names)

# COMMAND ----------

df.write.format("delta").mode("overwrite").saveAsTable("b_shealth")

# COMMAND ----------

# %sql
# select count(1) from b_shealth
