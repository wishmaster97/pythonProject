from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\Wish_Master\\Desktop\\WebDrivers\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.google.com")

driver.find_element(By.XPATH, "//input[@title='Search'][1]").send_keys("Hello World")
driver.find_element(By.CSS_SELECTOR, "div[class='FPdoLc lJ9FBc'] input[name='btnK']").click()

a_elements = driver.find_elements(By.TAG_NAME, "a")
print(len(a_elements))
driver.close()

