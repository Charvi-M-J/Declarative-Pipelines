# import dlt
# from pyspark.sql.functions import *

# @dlt.view(name="products_enr_view")
# def sales_stg_trns():
#     df = spark.readStream.table("products_stg")
#     df = df.withColumn("price", col("price").cast(IntegerType()))
#     return df


# dlt.create_streaming_table(
#     name = 'products_enr'
# )

# dlt.create_auto_cdc_flow(
#     target = "products_enr",
#     source = "products_enr_view",
#     keys = ["product_id"],
#     sequence_by = "last_updated",
#     ignore_null_updates = False,
#     apply_as_deletes = None,
#     apply_as_truncates = None,
#     column_list = None,
#     except_column_list = None,
#     stored_as_scd_type = 1,
#     track_history_column_list = None,
#     track_history_except_column_list = None
# )

import dlt
from pyspark.sql.functions import col
from pyspark.sql.types import IntegerType

@dlt.view(name="products_enr_view")
def products_enr_view():
    df = spark.readStream.table("products_stg")
    df = df.withColumn("price", col("price").cast(IntegerType()))
    return df

# Create the target streaming table
dlt.create_streaming_table(
    name='products_enr'
)

# Define CDC flow
dlt.create_auto_cdc_flow(
    target="products_enr",
    source="products_enr_view",
    keys=["product_id"],
    sequence_by=col("last_updated"),  # ✅ safer than a string
    ignore_null_updates=False,
    stored_as_scd_type=1
)
