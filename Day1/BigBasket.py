from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\\Users\\Wish_Master\\Desktop\\WebDrivers\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.bigbasket.com")

wait = WebDriverWait(driver, 10)
#elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@qa='product_name']")))
#print(type(elements))

#anchors = list(driver.find_elements(By.XPATH("//div/a[@class='ng-binding']"))
elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div/a[@class='ng-binding']")))

print(type(elements))
for i in elements:
    ind = elements.index(i)
    if i.text == "Cauliflower":
        print(f" Index : {ind} , Text : {i.text}")
        driver.find_elements(By.XPATH, "//div[@qa='qty']/input").__getitem__(ind).clear()
        print("CLear")
        #driver.find_element(By.XPATH, f"(//div[@qa='qty']/input)[{ind}]").send_keys("2")
        driver.find_elements(By.XPATH, "//div[@qa='qty']/input").__getitem__(ind).send_keys(2)
        print("2 Added")
        #driver.find_element(By.XPATH, f"(//button[@type='button'][normalize-space()='Add'])[{ind}]").click()
        driver.find_elements(By.XPATH, "//button[@type='button'][normalize-space()='Add']").__getitem__(ind).click()
        print("Button Added")

driver.close()