CREATE OR REPLACE VIEW raw_products AS
SELECT *
FROM read_parquet("~/Projects/rig_value_guide/data/raw/*/*.parquet");
