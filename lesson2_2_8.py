from selenium import webdriver
import math
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    # 'C:\webdriver\chromedriver'
    driver = webdriver.Chrome()
    driver.get(link)

    input1 = driver.find_element_by_name('firstname')
    input1.send_keys("Ivan")
    input2 = driver.find_element_by_name('lastname')
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_name('email')
    input3.send_keys("a@a.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'requirements.txt')  # добавляем к этому пути имя файла
    input4 = driver.find_element_by_name('file')
    input4.send_keys(file_path)
    button = driver.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    driver.quit()
