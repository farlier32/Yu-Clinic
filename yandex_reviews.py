from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time


url = "https://yandex.by/maps/org/yu_klinik/180376536625/reviews/?ll=31.022034%2C52.467901&z=16"
driver = webdriver.Edge()

review = []
try:
    driver.get(url=url)
    time.sleep(15)

    review_list = driver.find_elements(By.CLASS_NAME, value="business-review-view__body-text")
    for i in review_list:
        review.append(f"{i.text}\n")

except Exception as ex:
    print(ex)
with open('selenium_python/reviews.txt', 'w', encoding="utf-8") as f:
    f.writelines(review)