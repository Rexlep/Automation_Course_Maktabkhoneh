from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://maktabkhooneh.org/")

current_url = driver.current_url
page_title = driver.title
page_source = driver.page_source
print(current_url)
print(page_title)
print(page_source)

driver.close()
driver.quit()