import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'https://SunInJuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID,'input_value').text
    browser.execute_script("window.scrollBy(0, 100);")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(x))
    for  val in 'robotCheckbox', 'robotsRule':
        browser.find_element(By.CSS_SELECTOR,f'[for="{val}"]').click()


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()