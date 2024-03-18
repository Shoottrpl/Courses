from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)

    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

    x = int(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.ID, 'answer').send_keys(calc(x))

    submit = browser.find_element(By.TAG_NAME, 'button')
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

