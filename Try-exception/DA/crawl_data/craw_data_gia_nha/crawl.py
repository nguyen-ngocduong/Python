import pandas as pd
import numpy as np
import logging
from time import sleep
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
import undetected_chromedriver as uc

logging.basicConfig(
    filename= 'app.log',
    level= logging.INFO,
    format= '%(asctime)s - %(levelname)s - %(message)s'
)
logging.info('=========== Starting the crawl data script ===========')

def chrome_webdriver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Chạy Chrome không hiển thị giao diện
    options.add_argument('--disable-gpu') # Tắt GPU tăng hiệu suất
    options.add_argument("--no-sandbox")  # Tránh lỗi sandbox trong môi trường Linux
    options.add_argument("--disable-blink-features=AutomationControlled")  # Giảm khả năng phát hiện bot
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")  # User-agent giả lập trình duyệt thật
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-plugins")
    options.add_argument("--disable-images")  # Tắt tải hình ảnh để tăng tốc

    driver = uc.Chrome(options=options)
    return driver

def craw_link_news(browser, link_url):
    '''
        Crawl danh sách link tin đăng bất động sản từ trang kết quả.
    '''
    try:
        browser.get(link_url)
        sleep(5)  # Hoặc dùng WebDriverWait nếu muốn chắc chắn dữ liệu đã load

        news_links = []

        # Lấy tất cả các thẻ sản phẩm theo selector đúng
        cards = browser.find_elements(By.CSS_SELECTOR, ".js__card.js__card-full-web")

        for card in cards:
            try:
                # Tìm thẻ <a> bên trong mỗi card
                a_tag = card.find_element(By.CSS_SELECTOR, "a.js__product-link-for-product-id")
                href = a_tag.get_attribute("href")
                
                # Nếu là link tương đối, nối với domain
                if href.startswith("/"):
                    href = "https://batdongsan.com.vn" + href

                news_links.append(href)
            except Exception as e:
                logging.warning(f"Lỗi khi lấy link từ card: {e}")
                continue

        return news_links

    except Exception as e:
        logging.error(f'Error when run craw_link_news: {e}')
        return []
def craw_info_news(browser, url):
    """
    Truy cập vào link và crawl dữ liệu chi tiết bài đăng bất động sản.
    """
    browser.get(url)
    sleep(3)  # Cho trang load sơ bộ
    
    try:
        # ⏳ Đợi tiêu đề xuất hiện
        elem = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".re__pr-title.pr-title.js__pr-title"))
        )
        name = elem.text.strip()
    except Exception as e:
        print("❌ Không tìm thấy tiêu đề — dump HTML để debug:")
        print(browser.page_source[:2000])
        logging.error(f"Lỗi tìm tiêu đề: {e}")
        return {}

    # ✅ Nếu có tiêu đề → tiếp tục lấy dữ liệu khác
    sleep(1)
    try:
        # Địa chỉ
        location = browser.find_element(By.CSS_SELECTOR, ".re__pr-short-description.js__pr-address").text.strip()
    except Exception:
        location = ""

    # Thông tin ngắn (diện tích, giá, v.v.)
    short_items = browser.find_elements(By.CSS_SELECTOR, ".re__pr-short-info-item")
    price, area = "", ""

    for item in short_items:
        try:
            title = item.find_element(By.CSS_SELECTOR, ".title").text.strip()
            value = item.find_element(By.CSS_SELECTOR, ".value").text.strip()

            # Dùng find_elements để tránh lỗi nếu không có '.ext'
            ext_elements = item.find_elements(By.CSS_SELECTOR, ".ext")
            ext = ext_elements[0].text.strip() if ext_elements else ""

            if title == "Diện tích":
                area = f"{value} {ext}".strip()
            elif title in ["Giá", "Khoảng giá"]:
                price = f"{value} {ext}".strip()
        except Exception as inner_e:
            logging.warning(f"Lỗi nhỏ trong short_item: {inner_e}")
            continue

    # Ngày xác thực
    verified_elements = browser.find_elements(By.CSS_SELECTOR, ".re__pr-listing-verified-section.re__section")
    time_verified = ""
    for el in verified_elements:
        text = el.text.strip()
        if text:
            match = re.search(r"\d{2}/\d{2}/\d{4}", text)
            if match:
                time_verified = match.group()

    return {
        'name': name,
        'location': location,
        'price': price,
        'area': area,
        'time': time_verified
    }
if __name__ == "__main__":
    driver = chrome_webdriver()
    proxies = ["https://batdongsan.com.vn/nha-dat-ban-ha-noi/gia-tu-1-ty-den-2-ty",
               "https://batdongsan.com.vn/nha-dat-ban-ha-noi/gia-tu-2-ty-den-3-ty",
               "https://batdongsan.com.vn/nha-dat-ban-ha-noi/gia-tu-3-ty-den-5-ty",
               "https://batdongsan.com.vn/nha-dat-ban-ha-noi/gia-tu-5-ty-den-7-ty",
               "https://batdongsan.com.vn/nha-dat-ban-ha-noi/gia-tu-7-ty-den-10-ty",
               "https://batdongsan.com.vn/nha-dat-ban-ha-noi/gia-tu-10-ty-den-20-ty"]
    # Crawl link 
    All_links = []
    for link in proxies:
        news_link = craw_link_news(driver, link)
        for url in news_link:
            All_links.append(url)
    with open('file_pth.pth(1)', 'w', encoding='utf-8') as f:
        for link in All_links:
            f.write(link + '\n')
    results = []
    for link in All_links:
        res = craw_info_news(driver, link)
        results.append(res)
    # Lưu dữ liệu vào CSV
    df = pd.DataFrame(results)
    df.to_csv('batdongsan_data(1).csv', index=False, encoding='utf-8-sig')
    logging.info(f"Lưu {len(df)} dòng dữ liệu vào batdongsan_data(1).csv")
    driver.quit()
