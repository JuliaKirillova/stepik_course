from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:

    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector("[id='book']")
    button = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID,'price'), '$100'))
    button = browser.find_element_by_css_selector("[id='book']")
    button.click()
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
