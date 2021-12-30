from selenium import webdriver
import time
import math
import os

    
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
browser.find_element_by_xpath("/html/body/div/form/div/input[1]").send_keys("y")
browser.find_element_by_xpath("/html/body/div/form/div/input[2]").send_keys("y")
browser.find_element_by_xpath("/html/body/div/form/div/input[3]").send_keys("y")


#вставляем файл из той-же директории где лежит скрипт

# получаем путь к директории текущего исполняемого скрипта
current_dir = os.path.abspath(os.path.dirname(__file__))

# имя файла, который будем загружать на сайт
file_name = "1.txt"

# получаем путь к file_example.txt
file_path = os.path.join(current_dir, file_name)
# отправляем файл
browser.find_element_by_xpath("//*[@id='file']").send_keys(file_path)

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()


# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()