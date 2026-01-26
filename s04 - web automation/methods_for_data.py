from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://maktabkhooneh.org/")

element = driver.find_element(By.XPATH, 'html/body/div[1]/section/main/section/div/div[1]/div[1]/div[1]/h4')

text = element.text
attribute = element.get_attribute('class')
css_value = element.value_of_css_property("font")
location = element.location
size = element.size

print(attribute)
print(element.text)
print(css_value)
print(location)
print(size)