from selenium import webdriver
from selenium.webdriver.support.ui import Select

import math, time

url = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)
    num1 = int(browser.find_element_by_id("num1").text)
    num2 = int(browser.find_element_by_id("num2").text)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(num1 + num2))
    btn = browser.find_element_by_css_selector(".btn")
    btn.click()


finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()
