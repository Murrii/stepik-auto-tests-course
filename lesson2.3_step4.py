from selenium.webdriver.chrome.webdriver import WebDriver
import math


# Открыть страницу http://suninjuly.github.io/alert_accept.html
con = WebDriver()
con.get("http://suninjuly.github.io/alert_accept.html")

# находим кнопку на странице
journey_btn = con.find_element_by_css_selector('[type="submit"]')

# Нажать на кнопку
journey_btn.click()

# Принять confirm
con.switch_to.alert.accept()

# находим веб-элементы на новой странице
x_variable = con.find_element_by_css_selector('#input_value')
answer_text_field = con.find_element_by_css_selector('#answer')
submit_btn = con.find_element_by_css_selector('[type="submit"]')

# получаем переменную х
x = int(x_variable.text)

# решаем пример
answer = math.log((abs(12*math.sin(x))))

# вводим данные в поле ввода
answer_text_field.send_keys(str(answer))

# отправляем форму
submit_btn.click()
