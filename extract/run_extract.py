from bs4 import BeautifulSoup
import requests
import pandas as pd

products = pd.read_csv("/home/siegfried/Projects/rig_value_guide/seeds/source_targets.csv")

def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    return soup

def raw_name_extract(soup):
    raw_name = soup.find("h1", class_="product-title")

    return raw_name.text if raw_name else None

def raw_id_extract(soup):
    raw_id = soup.find("li", class_="is-active")
# make more robust
    return raw_id.text[-15:] if raw_id else None

def raw_price_extract(soup):
    price = soup.find("div", class_="price-current")

    dollars = price.find("strong")
    cents = price.find("sup")

    return (dollars.text if dollars else "") + (cents.text if cents else "")

def build_raw_record(product, soup):
    return {
        "product_id": product["product_id"],
        "source_name": product["source_name"],
        "product_url": product["source_product_url"],
        "raw_product_id": raw_id_extract(soup),
        "product_name_raw": raw_name_extract(soup),
        "price_text_raw": raw_price_extract(soup),
        "observed_at":""
            }

records = []

for _, product in products.iterrows():
    soup = get_soup(product["source_product_url"])
    record = build_raw_record(product, soup)
    records.append(record)

raw_df = pd.DataFrame(records)
print(raw_df)
