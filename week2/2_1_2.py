from selenium import webdriver
import math, time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


url = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    img = browser.find_element_by_id("treasure")
    result = calc(img.get_attribute("valuex"))
    answer = browser.find_element_by_id("answer")
    answer.send_keys(result)
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    radio = browser.find_element_by_id("robotsRule")
    radio.click()
    btn = browser.find_element_by_css_selector("button[type='submit']")
    btn.click()



finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()
