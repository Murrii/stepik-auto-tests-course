from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.common.by import By
import math


# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
con = WebDriver()
con.get("http://suninjuly.github.io/explicit_wait2.html")

# Дождаться, когда цена дома уменьшится до 10000 RUR (ожидание нужно установить не меньше 12 секунд)
price = WebDriverWait(con, 12).until(text_to_be_present_in_element((By.ID, "price"), "10000"))

# Нажать на кнопку "Забронировать"
con.find_element_by_css_selector("#book").click()

# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

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
