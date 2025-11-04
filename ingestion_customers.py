import dlt

customers_rules = {
    "rule_1": "customer_id IS NOT NULL",
    "rule_2": "customer_name IS NOT NULL"
}
@dlt.table(
    name = "customers_stg"
)
@dlt.expect_all_or_drop(customers_rules)
def products_stg():

    df = spark.readStream.table("dltchar.sour.customers")
    return df