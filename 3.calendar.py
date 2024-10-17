# Databricks notebook source
from pyspark.sql.functions import *
from datetime import datetime, timedelta

# COMMAND ----------

startdate = datetime.strptime('2019-01-01','%Y-%m-%d')
enddate   = (datetime.now() + timedelta(days=365 * 3)).replace(month=12, day=31)


# COMMAND ----------

print(startdate)
print(enddate)

# COMMAND ----------

column_rule_df = spark.createDataFrame(
    [
        ("Date_Integer", "cast(date_format(date, 'yyyyMMdd') as int)"),  # 20230101
        ("Year", "year(date)"),  # 2023
        ("Quarter", "quarter(date)"),  # 1
        ("Month", "month(date)"),  # 1
        ("Day", "day(date)"),  # 1
        ("Week", "weekofyear(date)"),  # 1
        ("Quarter_Name", "concat(quarter(date),'º trimestre')") ,  # 1º trimestre
        ("Quarter_Name_Abb", "concat('T',quarter(date))") ,  # T1
        ("Quarter_Number_2d", "date_format(date, 'QQ')"),  # 01
        ("Month_Number_2d", "date_format(date, 'MM')"),  # 01
        ("Day_Number_2d", "date_format(date, 'dd')"),  # 01
        ("Week_Day_Number", "dayofweek(date)"),  # 1
        ("Year_Month", "date_format(date, 'yyyy/MM')"),  # 2023/01
        ("Month_Name_Full", "date_format(date, 'MMMM')"),
        ("Month_Name_Abb", "date_format(date, 'MMM')"),
        ("Weekday_Name", "date_format(date, 'EEEE')"),
        ("Weekday_Name_Abb", "date_format(date, 'E')")
    ],
    ["new_column_name", "expression"],
)

# COMMAND ----------

start = int(startdate.timestamp())
stop  = int(enddate.timestamp())
df = spark.range(start, stop, 60*60*24).select(col("id").cast("timestamp").cast("date").alias("Date"))

# COMMAND ----------

for row in column_rule_df.collect():
    new_column_name = row["new_column_name"]
    expression = expr(row["expression"])
    df = df.withColumn(new_column_name, expression)

# COMMAND ----------

# display(df)

# COMMAND ----------

df.write.mode("overwrite").saveAsTable("g_calendar")

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC -- select * from gold.dim_calendario
