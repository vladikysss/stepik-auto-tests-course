from selenium import webdriver
import time
import math

#Считаем значение по формуле 
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)


#жмем на кнопку
browser.find_element_by_css_selector("button.trollface").click()

#заводим страницы в переменные
new_window = browser.window_handles[1]
first_window = browser.window_handles[0]
#Переходим на новую вкладку
browser.switch_to.window(new_window)

x = browser.find_element_by_id("input_value").text
y = calc(int(x))

browser.find_element_by_id("answer").send_keys(y)    

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn").click()


# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()