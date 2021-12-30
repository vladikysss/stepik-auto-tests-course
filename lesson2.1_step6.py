from selenium import webdriver
import time
import math

#Считаем значение по формуле 
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
x = browser.find_element_by_id("treasure").get_attribute("valuex")
browser.find_element_by_id("robotCheckbox").click()
browser.find_element_by_id("robotsRule").click()
y = calc(int(x))
browser.find_element_by_id("answer").send_keys(y)    

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()


# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()