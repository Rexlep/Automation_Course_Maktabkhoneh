from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python automation")
search_box.send_keys(Keys.ENTER)

time.sleep(3)

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])

text_input = driver.find_element(By.NAME, "my-text")
password_input = driver.find_element(By.NAME, "password")
textarea = driver.find_element(By.NAME, "textarea")

text_input.send_keys("Automation in maktabkhooneh")
password_input.send_keys("123455678")
textarea.send_keys("selenium automation in python using pycharm in this course")

time.sleep(3)

text_input.clear()
password_input.clear()
textarea.clear()

time.sleep(3)

driver.quit()