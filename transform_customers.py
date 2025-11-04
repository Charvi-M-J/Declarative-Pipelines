import dlt
from pyspark.sql.functions import col, upper

@dlt.view(name="customers_enr_view")
def customers_enr_view():
    df = spark.readStream.table("customers_stg")
    df = df.withColumn("customer_name", upper(col("customer_name")))
    return df

# Define target streaming table
dlt.create_streaming_table(
    name="customers_enr"
)

# Create CDC flow
dlt.create_auto_cdc_flow(
    target="customers_enr",
    source="customers_enr_view",
    keys=["customer_id"],
    sequence_by=col("last_updated"),   
    ignore_null_updates=False,
    stored_as_scd_type=1               
)
