from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    first_name = browser.find_element_by_name("firstname")
    first_name.send_keys("text")
    last_name = browser.find_element_by_name("lastname")
    last_name.send_keys("text")
    email = browser.find_element_by_name("email")
    email.send_keys("text")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла

    element = browser.find_element_by_id("file")
    element.send_keys(file_path)

    btn = browser.find_element_by_tag_name("button")
    btn.click()


finally:
    time.sleep(10)
    browser.quit()
