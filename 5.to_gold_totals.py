# Databricks notebook source
from pyspark.sql.functions import year, month, weekofyear, sum, concat, date_format, lit

# COMMAND ----------

df = spark.read.format("delta").table("s_shealth")

# COMMAND ----------

# create a table aggregate by year, month and week
df_agg = (df.groupBy(date_format("start_time", "yyyy-mm-dd").alias('date'),
                     ("exercise_type"),
                     weekofyear("start_time").alias("week"))
          .agg(sum("calorie").alias("total_calorie"),
               sum("exercise_distance").alias("total_exercise_distance")))


# COMMAND ----------

df_agg.write.format("delta") \
    .option("mergeSchema", "true") \
    .mode("overwrite") \
    .saveAsTable("g_totals")

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC select min(date) from g_totals
