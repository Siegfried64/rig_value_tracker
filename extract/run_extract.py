from bs4 import BeautifulSoup
import requests

# Replace hardcoded list with logic for extracting source seed records
products = [{"product_id": "gpu_rtx5090", "category": "GPU", "brand_name": "NVIDIA", "name": "GeForce RTX 5090", "tier": "high"}]

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

#ToDo - Change hardcoded source to use source seed
gpu_5090 = "https://www.newegg.com/gigabyte-gv-n5090gaming-oc-32gd-geforce-rtx-5090-32gb-graphics-card-triple-fans/p/N82E16814932761"

# Create dictionary build function in order to loop through all products
soup = get_soup(gpu_5090)

raw_dict = {
    "raw_product_id": raw_id_extract(soup),
    "product_name_raw": raw_name_extract(soup),
    "brand_raw":"",
    "category_raw":"",
    "price_text_raw": raw_price_extract(soup),
    "price_value":"",
    "currency":"",
    "availability_raw":"",
    "product_url": gpu_5090,
    "observed_at":""
    }

print(raw_dict)
