# Databricks notebook source
dbutils.widgets.text("catalog", "main")
dbutils.widgets.text("schema", "dab_demo")
dbutils.widgets.text("table_name", "customer_events")

catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")
table_name = dbutils.widgets.get("table_name")

full_schema = f"{catalog}.{schema}"
full_table = f"{catalog}.{schema}.{table_name}"

spark.sql(f"CREATE SCHEMA IF NOT EXISTS {full_schema}")

spark.sql(f"""
CREATE TABLE IF NOT EXISTS {full_table} (
  event_id BIGINT,
  customer_id BIGINT,
  event_type STRING,
  amount DOUBLE,
  event_date DATE,
  inserted_at TIMESTAMP
)
USING DELTA
""")

spark.sql(f"""
CREATE OR REPLACE VIEW {catalog}.{schema}.v_customer_event_summary AS
SELECT
  event_type,
  COUNT(*) AS row_count,
  ROUND(SUM(amount), 2) AS total_amount
FROM {full_table}
GROUP BY event_type
""")

print(f"Created schema if needed: {full_schema}")
print(f"Created table if needed: {full_table}")
print(f"Created or replaced view: {catalog}.{schema}.v_customer_event_summary")
