from rig_value_guide.common import config as conf

cfg = conf.load_config()
# raw extracted data
sql_vars = {
    "raw_newegg_path": str(cfg["paths"]["raw_extract"] / "newegg" / "*.parquet")
}
# sql logic files
sql_path = cfg["paths"]["sql_raw"] / "raw_products.sql"

sql = sql.format(**sql_vars)
