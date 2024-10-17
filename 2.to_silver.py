# Databricks notebook source
df = spark.read.format("delta").table("b_shealth").selectExpr(
    "CAST(start_time AS TIMESTAMP) as start_time",
    "CAST(exercise_type AS INT) as exercise_type",
    "COALESCE(CAST(distance AS INT),0) as exercise_distance",
    "CAST(calorie AS INT) as calorie"
    )

# COMMAND ----------

df = df.filter("exercise_type > 0")

# COMMAND ----------

df.write.format("delta").mode("overwrite").saveAsTable("s_shealth")
