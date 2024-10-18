# Databricks notebook source
from pyspark.sql.functions import year, month, weekofyear, sum, concat, to_date, lit

# COMMAND ----------

df = spark.read.format("delta").table("s_shealth")

# COMMAND ----------

display(df.limit(100))

# COMMAND ----------

from pyspark.sql.functions import to_date, sum

# create a table aggregate by year, month and week
df_agg = (df.groupBy(to_date("start_time").alias('date'), "exercise_type")
             .agg(sum("calorie").alias("total_calorie"),
                  sum("exercise_distance").alias("total_exercise_distance")))

display(df_agg)

# COMMAND ----------

df_agg.write.format("delta") \
    .option("mergeSchema", "true") \
    .mode("overwrite") \
    .saveAsTable("g_totals")

# COMMAND ----------

# %sql

# select min(date) from g_totals
