from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select

# Открыть браузер
con = WebDriver()

# Открыть страницу http://suninjuly.github.io/selects1.html
con.get("http://suninjuly.github.io/selects1.html")

# Найти веб-элементы с числами, выпадающим списком и кнопкой
first_num_el = con.find_element_by_css_selector("#num1")
second_num_el = con.find_element_by_css_selector("#num2")

drop_list = Select(con.find_element_by_css_selector("select"))

submit_btn = con.find_element_by_css_selector("[type='submit']")

# Посчитать сумму заданных чисел
sum = int(first_num_el.text) + int(second_num_el.text)

# Выбрать в выпадающем списке значение равное расчитанной сумме
drop_list.select_by_visible_text(str(sum))

# Нажать кнопку "Отправить"
submit_btn.click()

