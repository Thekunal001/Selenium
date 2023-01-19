#  THIS TEST CASE IS FOR THE INVALID EMAIL AND VALID PASOWRD

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://inuvest.tech/")
# driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH, "//*[@id='navbarBasicExample']/div[2]/div/div[2]/a[1]").click()
driver.find_element(By.XPATH, "//*[@id='first']/div[1]/div/input").send_keys("ENTER INVALID EMAIL")
driver.find_element(By.XPATH, "//*[@id='first']/div[2]/div/input").send_keys("ENTER VALID PASSWORD")
driver.find_element(By.XPATH, "//*[@id='first']/div[3]/button").click()
Text = driver.find_element(By.XPATH, "//*[@id='swal2-title']").text

if Text == "Wrong username or password":
    print("test Passed")
else:
    print("test failed")
time.sleep(5)
driver.quit()
