import os 
import re
import ast
import argparse
import logging
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime

#logging
logging.basicConfig(
    filename= 'log/app.log',
    level= logging.INFO,
    format= '%(asctime)s - %(levelname)s - %(message)s'
)
logging.info("============== Log file ==============")

def chrome_webdriver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Chạy Chrome không hiển thị giao diện
    options.add_argument("--disable-gpu")  # Tắt GPU tăng hiệu suất
    options.add_argument("--no-sandbox")  # Tránh lỗi sandbox trong môi trường Linux

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# show more
def show_more(browser):
    """
    Click tu dong vao not xem them
    """
    try:
        while 1:
            browser.find_element(By.CSS_SELECTOR, ".see-more-btn").click()
            sleep(3)
    except Exception as e:
        logging.error(f"Can not find HTML element {e}")

def craw_product_link(browser, url):
    """
    craw link cua tung product
    """
    browser.get(url)
    sleep(3)
    show_more(browser)
    sleep(3)
    productions_links = []
    try: 
        products = browser.find_elements(By.CSS_SELECTOR, '.item.__cate_1942')
        for product in products:
            product_link = product.find_element(By.TAG_NAME, 'a').get_attribute('href')
            productions_links.append(product_link)
        return productions_links
    except Exception as e:
        logging.error(f'Error when run craw_product_link function {e}')
#craw name, price
def craw_name_price_rate(browser, url):
    """
    Truy cập vào trang danh sách sản phẩm để lấy tên, giá, và đánh giá
    """
    browser.get(url)
    sleep(3)
    show_more(browser)
    sleep(3)
    names, rates, prices = [], [], []
    try:
        product_items = browser.find_elements(By.CSS_SELECTOR, 'a.main-contain')
        for item in product_items:
            try:
                name_el = item.find_element(By.CSS_SELECTOR, 'h3')
                name = name_el.get_attribute("title") or name_el.text.strip()
            except:
                name = ""
            try:
                price_el = item.find_element(By.CSS_SELECTOR, 'strong.price')
                price = price_el.text.strip()
            except:
                price = ""
            try:
                rate_el = item.find_element(By.CSS_SELECTOR, '.vote-txt b')
                rate = rate_el.text.strip()
            except:
                rate = "Chưa có đánh giá"
            names.append(name)
            prices.append(price)
            rates.append(rate)
        return names, prices, rates
    except Exception as e:
        logging.error(f"Không thể crawl tên, giá hoặc đánh giá sản phẩm: {e}")
        return [], [], []
    
def craw_description(browser, product_link):
    """
    Truy cập từng link để lấy mô tả sản phẩm (Thông số kỹ thuật)
    Trả về dictionary: { "Tên thông số": "Giá trị", ... }
    """
    browser.get(product_link)
    sleep(3)

    specifications = {}

    try:
        # Tìm tất cả các mục thông số
        spec_sections = browser.find_elements(By.CSS_SELECTOR, 'div.box-specifi')

        for section in spec_sections:
            # Mỗi section có nhiều <li>
            lis = section.find_elements(By.TAG_NAME, 'li')
            for li in lis:
                try:
                    key_element = li.find_element(By.CSS_SELECTOR, 'aside strong')
                    key = key_element.text.strip().replace(":", "")

                    value_aside = li.find_elements(By.CSS_SELECTOR, 'aside')[1]
                    # Lấy toàn bộ text trong <a> hoặc <span>
                    value_parts = value_aside.find_elements(By.CSS_SELECTOR, 'a, span')
                    value = ", ".join([v.text.strip() for v in value_parts if v.text.strip()])

                    # Nếu không có <a> hoặc <span>, lấy toàn bộ text trong aside
                    if not value:
                        value = value_aside.text.strip()

                    if key and value:
                        specifications[key] = value

                except Exception as e:
                    logging.warning(f"Lỗi khi đọc 1 dòng thông số: {e}")
                    continue

        return specifications

    except Exception as e:
        logging.error(f'Lỗi ở hàm craw_description: {e}')
        return {}

def craw_info_product(browser, url):
    """
    Truy cap vao tung link va lay ra thong tin can thiet
    """
    browser.get(url)
    sleep(3)
    product_link = craw_product_link(browser,url)
    names, rates, prices = craw_name_price_rate(browser, url)
    product_description = []
    for link in product_link:
        description = craw_description(browser, link)
        product_description.append(description)
    return {
        'name' : names,
        'price' : prices,
        'rate' : rates,
        'description': product_description,
        'link_product': product_link
    }

def scrape_dienmayxanh():
    url = 'https://www.dienmayxanh.com/tivi-samsung-qled'
    browser = chrome_webdriver()
    data = craw_info_product(browser, url)
    df = pd.DataFrame(data)
    df.to_csv('data/craw_dmx.csv', index = True)
    print('Done!')

if __name__ == '__main__':
    scrape_dienmayxanh()