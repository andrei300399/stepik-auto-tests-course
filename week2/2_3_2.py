from selenium import webdriver

import time, math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


url = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    btn = browser.find_element_by_class_name("trollface")
    btn.click()

    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element_by_id("input_value").text
    answer = browser.find_element_by_id("answer")
    answer.send_keys(calc(x))

    btn = browser.find_element_by_class_name("btn-primary")
    btn.click()


finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()
