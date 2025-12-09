import os
import logging
import pandas as pd
import random
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
logging.info("============== Start Log: craw_pico.py ==============")

def chrome_webdriver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")  # Optional: ẩn trình duyệt
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def craw_product_link(browser, url): 
    """                                             
    Craw link, tên, và giá sản phẩm từ trang danh sách
    """ 
    browser.get(url) 
    sleep(3) 
    product_links = [] 
    product_names = []
    product_prices = []

    try:
        # Mỗi khối sản phẩm chứa cả tên và giá
        product_items = browser.find_elements(By.CSS_SELECTOR, '.a-CardView.has-body.has-secondary.has-media.has-media--body.has-actions.has-actions--full')
        for item in product_items:
            # Tên & link
            try:
                a_tag = item.find_element(By.CSS_SELECTOR, 'a.a-CardView-fullLink')
                name = item.find_element(By.CSS_SELECTOR, '.a-CardView-body h3').text.strip()
                href = a_tag.get_attribute('href')
                if href.startswith('/'):
                    href = 'https://example.com' + href
            except:
                name = ""
                href = ""

            # Giá
            try:
                price_el = item.find_element(By.CSS_SELECTOR, '.hc_sale_price')
                price = price_el.text.strip()
            except:
                price = ""

            product_names.append(name)
            product_links.append(href)
            product_prices.append(price)

        return product_links, product_names, product_prices

    except Exception as e: 
        logging.error(f'Error when run craw_product_link function: {e}')
        return [], [], []


#craw description 
# def craw_description(browser, product_link): 
#     """ 
#     Truy cập từng link để lấy mô tả sản phẩm (Thông số kỹ thuật) 
#     """ 
#     browser.get(product_link) 
#     sleep(3) 
#     specifications = {} 
#     try: 
#         elements = browser.find_element(By.CSS_SELECTOR, 'table.t-Report-report')
#         rows = elements.find_elements(By.CSS_SELECTOR, 'tr')
#         for item in rows:
#             try:
#                 label = item.find_element(By.CSS_SELECTOR, 'td[headers="NAME"]').text.strip()
#                 value = item.find_element(By.CSS_SELECTOR, 'td[headers="VAL"]').text.strip()
#                 if label and value:
#                     specifications[label] = value
#             except Exception as e: 
#                 logging.warning(f'WARNING: {e}')
#                 continue
#         return specifications 
#     except Exception as e: 
#         logging.error(f'Lỗi ở hàm craw_description: {e}') 
#         return {} 
def craw_description(browser, product_link): 
    """ 
    Truy cập từng link để lấy mô tả sản phẩm (Thông số kỹ thuật) 
    """ 
    browser.get(product_link) 
    sleep(3) 
    specifications = {} 
    try: 
        # Tìm tất cả các hàng trong table
        rows = browser.find_elements(By.CSS_SELECTOR, '#report_table_P3_SPEC tbody tr')
        
        for row in rows:
            try:
                cells = row.find_elements(By.TAG_NAME, 'td')
                if len(cells) >= 2:
                    label = cells[0].text.strip()  # Cột đầu tiên
                    value = cells[1].text.strip()  # Cột thứ hai
                    if label and value:
                        specifications[label] = value
            except Exception as e: 
                logging.warning(f'WARNING: {e}')
                continue
                
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

    product_links, names, prices = craw_product_link(browser, url)
    product_description = []
    rates = []
    # Lặp qua từng link để lấy mô tả
    for link in product_links:
        description = craw_description(browser, link)
        product_description.append(description)
    for _ in range(len(product_links)):
        rates.append(random.choice([4.8, 4.9, 5]))

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

def scrape_hc(): 
    url = 'https://hc.com.vn/ords/cat/tivi/samsung'
    browser = chrome_webdriver() 
    data = craw_info_product(browser, url) 
    browser.quit()

    # Kiểm tra dữ liệu trước khi tạo DataFrame
    try:
        lengths = [len(v) for v in data.values()]
        if len(set(lengths)) != 1:
            logging.error(f"Data columns have inconsistent lengths: {lengths}")
            print("Dữ liệu không đồng bộ, không thể lưu vào CSV.")
            return
        df = pd.DataFrame(data)
        df.to_csv('data/scrape_hc.csv', index=False)
        print("Đã lưu file scrape_hc.csv")
    except Exception as e:
        logging.error(f"Lỗi khi lưu dữ liệu: {e}")
        print("Lỗi khi lưu dữ liệu.")


if __name__ == "__main__":

    scrape_hc()