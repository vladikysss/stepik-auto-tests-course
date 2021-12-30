from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
#Считаем значение по формуле 
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
x = browser.find_element_by_id("num1").text
y = browser.find_element_by_id("num2").text
sum = int(x) + int(y)
print(sum)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(sum))
#select.select_by_visible_text(sum)
#browser.select_by_visible_text(sum)  

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()


# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()