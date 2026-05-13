CREATE OR REPLACE VIEW raw_products AS
SELECT *
FROM read_parquet("{raw_newegg_path}");
