from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
#Считаем значение по формуле 
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля

x = browser.find_element_by_id("input_value").text
y = calc(x)
browser.find_element_by_id("answer").send_keys(y)


#скролл до элемента
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)


browser.find_element_by_id("robotCheckbox").click()
browser.find_element_by_id("robotsRule").click()

# Отправляем заполненную форму
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button = browser.find_element_by_css_selector("button.btn")
button.click()


# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()