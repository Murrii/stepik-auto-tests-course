from selenium.webdriver.chrome.webdriver import WebDriver
import math

# Открыть страницу http://SunInJuly.github.io/execute_script.html.
con = WebDriver()
con.get("http://SunInJuly.github.io/execute_script.html")

# найти все видимые элементы на странице
x_variable = con.find_element_by_css_selector("#input_value")
answer_text_field = con.find_element_by_css_selector("#answer")
checkbox = con.find_element_by_css_selector("#robotCheckbox")

# Считать значение для переменной x.
x = int(x_variable.text)

# Посчитать математическую функцию от x.
result = math.log(abs(12 * math.sin(x)))

# Ввести ответ в текстовое поле.
answer_text_field.send_keys(str(result))

# Выбрать checkbox "Подтверждаю, что являюсь роботом".
checkbox.click()

# Проскроллить страницу вниз.
radio_btn = con.find_element_by_css_selector("#robotsRule")
con.execute_script("return arguments[0].scrollIntoView(true);", radio_btn)

# Переключить radiobutton "Роботы рулят!".
radio_btn.click()

# Нажать на кнопку "Отправить".
con.find_element_by_css_selector("[type='submit']").click()
