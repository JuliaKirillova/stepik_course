from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    option3 = browser.find_element_by_css_selector("[type='submit']")
    option3.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    answer = browser.find_element_by_id('answer')
    answer.send_keys(calc(x))
    option3 = browser.find_element_by_css_selector("[type='submit']")
    option3.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

