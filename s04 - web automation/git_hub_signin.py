from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://github.com/login")

time.sleep(8)

username = driver.find_element(By.NAME, "login")
username.send_keys("test@test.com")

password = driver.find_element(By.NAME, "password")
password.send_keys("12345678")

submit = driver.find_element(By.NAME, "commit")
submit.click()