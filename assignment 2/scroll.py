from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://inuvest.tech/")

driver.maximize_window()
driver.implicitly_wait(30)

price = driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/nb-layout-column/div/div/app-home/div/div[2]/div[14]/div/p")
driver.execute_script("arguments[0].scrollIntoView();", price)
driver.find_element(By.XPATH, "/html/body/app-root/nb-layout/nb-layout-column/div/div/app-home/div/div[3]/button[3]").click()
print("Test passed")