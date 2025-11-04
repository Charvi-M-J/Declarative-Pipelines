import dlt

products_rules = {
    "rule_1": "product_id IS NOT NULL",
    "rulr_2": "price >= 0"
}
@dlt.table(
    name = "products_stg"
)
@dlt.expect_all(products_rules)
def products_stg():

    df = spark.readStream.table("dltchar.sour.products")
    return df