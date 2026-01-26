import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://maktabkhooneh.org/")


input_site = driver.find_element(By.TAG_NAME, "input")
input_site.send_keys("امیر مهدی گودرزی")

input()