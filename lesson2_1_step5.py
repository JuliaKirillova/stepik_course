from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    # Отправляем заполненную форму
    option = browser.find_element_by_id('answer')
    option.send_keys(y)
    option1 = browser.find_element_by_css_selector("[type='checkbox']")
    option1.click()
    option2 = browser.find_element_by_css_selector("[value='robots']")
    option2.click()
    option3 = browser.find_element_by_css_selector("[type='submit']")
    option3.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()