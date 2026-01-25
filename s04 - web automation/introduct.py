from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://maktabkhooneh.org/")
driver.maximize_window()
driver.print_page()

input()