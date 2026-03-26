from bs4 import BeautifulSoup
import requests

products = [{"product_id": "gpu_rtx5090", "category": "GPU", "brand_name": "NVIDIA", "name": "GeForce RTX 5090", "tier": "high"}]

def price_extract(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    price = soup.find("div", class_="price-current")

    dollars = price.find("strong")
    cents = price.find("sup")

    return dollars.text + cents.text

#ToDo - Change hardcoded source to use source seed
gpu_5090 = "https://www.newegg.com/gigabyte-gv-n5090gaming-oc-32gd-geforce-rtx-5090-32gb-graphics-card-triple-fans/p/N82E16814932761"


raw_dict = {
    "source_product_id":"",
    "product_name_raw":"",
    "brand_raw":"",
    "category_raw":"",
    "price_text_raw": price_extract(gpu_5090),
    "price_value":"",
    "currency":"",
    "availability_raw":"",
    "product_url":"",
    "observed_at":""
    }

print(raw_dict)
