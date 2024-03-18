import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import math



login = 'triplsix1337@gmail.com'
pw = 'iKUDPn=QqG%F4M,'

list_urls = [
'https://stepik.org/lesson/236895/step/1',
'https://stepik.org/lesson/236896/step/1',
'https://stepik.org/lesson/236897/step/1',
'https://stepik.org/lesson/236898/step/1',
'https://stepik.org/lesson/236899/step/1',
'https://stepik.org/lesson/236903/step/1',
'https://stepik.org/lesson/236904/step/1',
'https://stepik.org/lesson/236905/step/1',
]


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()

def auth_stepick(browser, login, pw):
    browser.find_element(By.CSS_SELECTOR, '#ember408').click()
    browser.find_element(By.NAME, 'login').send_keys(login)
    browser.find_element(By.NAME, 'password').send_keys(pw)
    browser.find_element(By.CSS_SELECTOR, '#login_form button').click()



@pytest.mark.parametrize('login, pw, link',[('triplsix1337@gmail.com', 'iKUDPn=QqG%F4M,', i) for i in list_urls])
def test_parametrisation(pw, login, link, browser):
    global result
    browser.get(link)
    answer = math.log(int(time.time()))
    auth_stepick(browser, login, pw)

    try:
        browser.find_element(By.CSS_SELECTOR, '[class="again-btn white"]').click()
    except:
        pass
    finally:
        browser.find_element(By.TAG_NAME, 'textarea').send_keys(answer)
        browser.find_element(By.CLASS_NAME, 'submit-submission').click()
        text_optional = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text

        assert text_optional == 'Correct!', f"{text_optional}"


















    