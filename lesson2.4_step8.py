from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

#Считаем значение по формуле 
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)


# говорим Selenium проверять в течение 20 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
#жмем на кнопку
browser.find_element_by_id("book").click()

x = browser.find_element_by_id("input_value").text
y = calc(int(x))

browser.find_element_by_id("answer").send_keys(y)    

# Отправляем заполненную форму
button = browser.find_element_by_id("solve").click()


# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()