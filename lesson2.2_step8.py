from selenium.webdriver.chrome.webdriver import WebDriver
import os


# Открыть страницу http://suninjuly.github.io/file_input.html
con = WebDriver()
con.get("http://suninjuly.github.io/file_input.html")

# получаем веб-элементы на странице
first_name_field = con.find_element_by_css_selector("[name='firstname']")
second_name_field = con.find_element_by_css_selector("[name='lastname']")
email_field = con.find_element_by_css_selector("[name='email']")

send_file_btn = con.find_element_by_css_selector("#file")
submit_btn = con.find_element_by_css_selector("[type='submit']")

# Заполнить текстовые поля: имя, фамилия, email
first_name_field.send_keys("Вася")
second_name_field.send_keys("Пупкин")
email_field.send_keys("Vasya@mail.ru")

# определяем путь к папке со скриптом и текстовым файлом
path_to_folder = os.path.abspath(os.path.dirname(__file__))

# определяем путь к файлу
path_to_file = os.path.join(path_to_folder, "text file.txt")

# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
send_file_btn.send_keys(path_to_file)

# Нажать кнопку "Отправить"
submit_btn.click()

