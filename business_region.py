import dlt
from pyspark.sql.functions import *

@dlt.table(
    name = "business_sales"
)
def business_sales():
    df_fact = spark.read.table("fact_sales")
    df_dimCust = spark.read.table("dim_customers")
    df_dimProd = spark.read.table("dim_products")
 
    df_agg = df_prun.groupBy("region","category").agg(sum("total_amount").alias("total_sales"))

    return df_agg
    