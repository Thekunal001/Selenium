# IN THIS TEST CASE WE WILL PASS ALL
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://inuvest.tech/")

driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.XPATH, "//*[@id='navbarBasicExample']/div[2]/div/div[2]/a[2]").click()
driver.find_element(By.XPATH, "//*[@id='first']/div[1]/div/input").send_keys("VALID NAME")
driver.find_element(By.XPATH, "//*[@id='first']/div[2]/div/input").send_keys("INVALID LAST NAME") # MEANS TYPE NUMBERS INSTEAD OF ALPHABETS
driver.find_element(By.XPATH, "//*[@id='first']/div[3]/div/input").send_keys("VALID PHONE NUMBER")
driver.find_element(By.XPATH, "//*[@id='first']/div[4]/div/input").send_keys("VALID EMAIL ID")
driver.find_element(By.XPATH, "//*[@id='first']/div[5]/div/input").send_keys("VALID PASSWORD")
driver.find_element(By.XPATH, "//*[@id='first']/div[7]/button").click()
confirmation = driver.find_element(By.XPATH, "//*[@id='swal2-title']").text
if confirmation == "Please enter alphabets in Last Name":
    print("test passed")
else:
    print("test failed")
driver.quit()
