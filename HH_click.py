"""Мой автокликер"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
s = Service("C:\\chromedriver.exe")

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('user-data-dir=C:\\Users\\Артем\\PycharmProjects\\stepik\\User Data')

url = 'https://hh.ru/?hhtmFrom=settings'
with webdriver.Chrome(service=s) as browser:
    browser.get(url=url)
    time.sleep(2)
    button_1 = browser.find_element(By.CLASS_NAME, 'supernova-navi-item_area-switcher-button')
    button_1.click()
    time.sleep(1)
    input_form = browser.find_element(By.TAG_NAME, 'input').send_keys('Россия')
    time.sleep(5)
    button_2 = browser.find_element(By.CLASS_NAME, 'area-switcher-autocomplete-item')

    button_2.click()
    time.sleep(1)

    input_form = browser.find_element(By.TAG_NAME, 'input').send_keys('Python разработчик')
    time.sleep(2)
    button_3 = browser.find_element(By.CLASS_NAME, 'supernova-search-submit-text')
    button_3.click()
    time.sleep(3)
    button_4 = browser.find_elements(By.XPATH, "//div[@class='vacancy-serp-actions']/a")
    for i in button_4:
        i.click()
        time.sleep(3)
        """input_form_2 = browser.find_element(By.TAG_NAME, 'input').send_keys(
            'Добрый день. Мне очень интересна Ваша вакансия, прошу рассмотреть мое резюме')
        time.sleep(3)"""

    time.sleep(4)
