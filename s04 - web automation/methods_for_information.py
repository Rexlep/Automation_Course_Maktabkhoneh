from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://maktabkhooneh.org/")

element = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/section/div/div[1]/div[1]/div[1]/h4")

text = element.text
attribute = element.get_attribute("class")
css_value = element.value_of_css_property("font-size")
location = element.location
size = element.size

print(text)
print(attribute)
print(css_value)
print(location)
print(size)