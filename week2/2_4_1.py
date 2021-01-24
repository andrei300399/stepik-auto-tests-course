from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time,math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

url = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button=browser.find_element_by_id("book")
    button.click()

    x = browser.find_element_by_id("input_value").text
    answer = browser.find_element_by_id("answer")
    answer.send_keys(calc(x))

    btn = browser.find_element_by_id("solve")
    btn.click()

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()
