# Databricks notebook source
dbutils.widgets.text("catalog", "main")
dbutils.widgets.text("schema", "dab_demo")
dbutils.widgets.text("table_name", "customer_events")

catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")
table_name = dbutils.widgets.get("table_name")
full_table = f"{catalog}.{schema}.{table_name}"

from pyspark.sql import functions as F
from src.dummy_rows import build_dummy_rows

rows = build_dummy_rows(10)
df = spark.createDataFrame(rows).withColumn("event_date", F.to_date("event_date"))

# Keep reruns idempotent for the exercise:
spark.sql(f"DELETE FROM {full_table}")

(
    df.withColumn("inserted_at", F.current_timestamp())
      .write
      .mode("append")
      .saveAsTable(full_table)
)

display(spark.sql(f"SELECT * FROM {full_table} ORDER BY event_id"))
print(f"Inserted {len(rows)} rows into {full_table}")
