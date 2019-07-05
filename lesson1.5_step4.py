import math
from selenium.webdriver.chrome.webdriver import WebDriver

string = str(math.ceil(math.pow(math.pi, math.e)*10000))

con = WebDriver()
con.get("http://suninjuly.github.io/find_link_text")
con.find_element_by_partial_link_text(string).click()

input1 = con.find_element_by_tag_name("input")
input1.send_keys("Ivan")
input2 = con.find_element_by_name("last_name")
input2.send_keys("Petrov")
input3 = con.find_element_by_class_name("city")
input3.send_keys("Smolensk")
input4 = con.find_element_by_id("country")
input4.send_keys("Russia")
button = con.find_element_by_css_selector("button.btn")
button.click()