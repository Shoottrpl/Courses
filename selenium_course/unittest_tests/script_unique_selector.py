from selenium import webdriver
from selenium.webdriver.common.by import By

import time

def registration(number_of_link):
    link = f"http://suninjuly.github.io/registration{number_of_link}.html"
    browser = webdriver.Chrome()
    browser.get(link)
    class_names = ('first_class', 'second_class', 'third_class')
    for name in class_names:
        element = browser.find_element(By.CSS_SELECTOR, f'.first_block .form-group.{name} .form-control')
        print(element.text)
        element.send_keys("Мой ответ")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    return welcome_text

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

if __name__ == "__main__":
    registration(number_of_link=input())