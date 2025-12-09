import pandas as pd
import numpy as np
import logging
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
def chrome_webdriver():
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')  # Chạy Chrome không hiển thị giao diện
    #options.add_argument('--disable-gpu') # Tắt GPU tăng hiệu suất
    options.add_argument("--no-sandbox")  # Tránh lỗi sandbox trong môi trường Linux

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver
driver = chrome_webdriver()
url = "https://batdongsan.com.vn/ban-dat-xa-hoa-thach/hon-2-ty-100m2-full-tho-cu-so-do-mat-tien-6-8m-tai-cnc-lac-gan-cho-ql21-trung-tam-hanh-chinh-pr44214237"
driver.get(url)
sleep(5)

# Lấy toàn bộ span trong phần xác thực
verified_elements = driver.find_elements(By.CSS_SELECTOR, ".re__pr-listing-verified-section span")

for el in verified_elements:
    text = el.text.strip()
    if text:  # bỏ qua thẻ trống
        print(">> Raw text:", text)
        match = re.search(r"\d{2}/\d{2}/\d{4}", text)
        if match:
            print("✅ Ngày xác thực:", match.group())

driver.quit()
