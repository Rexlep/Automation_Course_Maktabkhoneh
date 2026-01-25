from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.google.com/")

search_box = driver.find_element(By.ID, "APjFqb")
search_box.send_keys("maktabkhoneh")
search_box.send_keys(Keys.ENTER)

submit = driver.find_element(By.ID, "search")
submit.click()