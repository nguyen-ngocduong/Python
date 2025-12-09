import os
import logging
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from datetime import datetime

os.makedirs('log', exist_ok=True)
logging.basicConfig(
    filename='log/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.info("============== Start Log: craw_meta.py ==============")

def chrome_webdriver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")  # Optional: ẩn trình duyệt
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# show more 
def show_more(browser): 
    """ Click tu dong vao not xem them """ 
    try: 
        while 1: 
            browser.find_element(By.CSS_SELECTOR, ".list-product-catasub-more").click() 
            sleep(3) 
    except Exception as e: 
        logging.error(f"Can not find HTML element {e}")

def craw_product_link(browser, url): 
    """ craw link cua tung product """ 
    browser.get(url) 
    sleep(3) 
    show_more(browser) 
    sleep(3) 
    productions_links = [] 
    names = [] 
    xpath = '//*[@id="_products"]//a/h3' 
    try: 
        products = browser.find_elements(By.CSS_SELECTOR, '.prod-hl-name') 
        elements = browser.find_elements(By.XPATH, xpath) 
        for product in products: 
            product_link = product.find_element(By.TAG_NAME, 'a').get_attribute('href') 
            productions_links.append(product_link) 
        for el in elements: 
            name = el.text.strip() 
            names.append(name) 
        return productions_links, names 
    except Exception as e: 
        logging.error(f'Error when run craw_product_link function {e}')
        return [],[]

#craw name, price 
def craw_price_rate(browser, product_link): 
    """ Truy cập vào trang sản phẩm để lấy giá và đánh giá (rating) """ 
    browser.get(product_link) 
    sleep(3) 
    # Click xem thêm nếu có 
    try: 
        show_more(browser) 
        sleep(3) 
    except Exception: 
        pass 
    rates, prices = [], [] 
    try: # Lấy toàn bộ rating 
        rate_elements = browser.find_elements(By.XPATH, '//*[@id="_products"]//span[contains(@class, "rating-box")]') 
        for r in rate_elements: 
            title_attr = r.get_attribute('title') 
            if title_attr:
                rates.append(title_attr.strip())
            else:
                rates.append(None)
            # Lấy toàn bộ giá 
        price_elements = browser.find_elements(By.XPATH, '//*[@id="_products"]//span[contains(@class, "product-price-meta")]') 
        for p in price_elements: 
            prices.append(p.text.strip()) 
        return rates, prices 
    except Exception as e: 
        logging.error(f"Không thể crawl rate hoặc giá sản phẩm: {e}") 
        return [], []

#craw description 
def craw_description(browser, product_link): 
    """ Truy cập từng link để lấy mô tả sản phẩm (Thông số kỹ thuật) """ 
    browser.get(product_link) 
    sleep(3) 
    specifications = {} 
    try: 
        keys = browser.find_elements(By.CSS_SELECTOR, '.specs-left') 
        values = browser.find_elements(By.CSS_SELECTOR, '.specs-right') 
        # Duyệt theo cặp chỉ mục song song 
        for i in range(min(len(keys), len(values))): 
            key = keys[i].text.strip().replace(":", "") 
            value = values[i].text.strip() 
            if key and value: 
                specifications[key] = value 
        return specifications 
    except Exception as e: 
        logging.error(f'Lỗi ở hàm craw_description: {e}') 
        return {} 
def craw_info_product(browser, url):
    """
    Truy cập vào trang chính, lấy tất cả link sản phẩm,
    sau đó vào từng link để lấy mô tả chi tiết, giá và đánh giá.
    """
    browser.get(url)
    sleep(3)

    product_links, names = craw_product_link(browser, url)
    rates, prices = craw_price_rate(browser, url)  # Dữ liệu từ trang tổng
    product_description = []

    # Lặp qua từng link để lấy mô tả
    for link in product_links:
        description = craw_description(browser, link)
        product_description.append(description)

    #Cắt các list dài về cùng độ dài ngắn nhất để tránh lỗi
    min_len = min(len(names), len(prices), len(rates), len(product_description), len(product_links))
    names = names[:min_len]
    prices = prices[:min_len]
    rates = rates[:min_len]
    product_description = product_description[:min_len]
    product_links = product_links[:min_len]

    return {
        'name': names,
        'price': prices,
        'rate': rates,
        'description': product_description,
        'link_product': product_links
    }

def scrape_meta(): 
    url = 'https://meta.vn/tv-samsung-c3430?specs=112.48586' 
    browser = chrome_webdriver() 
    data = craw_info_product(browser, url) 
    browser.quit()
    print(data)

    # Kiểm tra dữ liệu trước khi tạo DataFrame
    try:
        lengths = [len(v) for v in data.values()]
        if len(set(lengths)) != 1:
            logging.error(f"Data columns have inconsistent lengths: {lengths}")
            print("Dữ liệu không đồng bộ, không thể lưu vào CSV.")
            return
        df = pd.DataFrame(data)
        df.to_csv('data/scrape_meta.csv', index=False)
        print("Đã lưu file scrape_meta.csv")
    except Exception as e:
        logging.error(f"Lỗi khi lưu dữ liệu: {e}")
        print("Lỗi khi lưu dữ liệu.")


if __name__ == "__main__":
    scrape_meta()