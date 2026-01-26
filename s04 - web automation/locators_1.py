from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://maktabkhooneh.org/")

driver.refresh()
current_url = driver.current_url
page_title = driver.title
page_source = driver.page_source

# element = driver.find_element(By.TAG_NAME, "input")
# element2 = driver.find_element(By.CLASS_NAME, "box")
# element3 = driver.find_element(By.XPATH, "/html/body.//")
# element4 = driver.find_element(By.CSS_SELECTOR, ".box")
# element5 = driver.find_element(By.ID, "box")
# element6 = driver.find_element(By.LINK_TEXT, "دوره های پایتون")

input_by_class = driver.find_element(By.CLASS_NAME, "w-full")

print(input_by_class)