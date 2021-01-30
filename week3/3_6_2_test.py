import time
import math
import pytest
from selenium import webdriver
result= ""


@pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('lesson', ["236895", "236896", "236897","236898","236899","236903", "236904","236905"])
def test_correct_answer(browser, lesson):
    global result
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.get(link)
    text_area = browser.find_element_by_css_selector(".string-quiz__textarea")
    answer = str(math.log(int(time.time())))
    text_area.send_keys(answer)
    button= browser.find_element_by_css_selector("button.submit-submission")
    button.click()
    text_answer = browser.find_element_by_css_selector(".smart-hints__hint").text
    if text_answer != "Correct!":
        result+=text_answer
        print(result)
