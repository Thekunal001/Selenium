#  THIS TEST CASE IS FOR THE VALID EMAIL AND VALID PASOWRD
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
driver.find_element(By.XPATH, "//*[@id='first']/div[1]/div/input").send_keys("ENTER VALID EMAIL")
driver.find_element(By.XPATH, "//*[@id='first']/div[2]/div/input").send_keys("ENTER VALID PASSWORD")
driver.find_element(By.XPATH, "//*[@id='first']/div[3]/button").click()
Dashboard = driver.find_element(By.XPATH, "//*[@id='navbarSupportedContent-3']/ul[1]/li[1]/a").text
if Dashboard == "Dashboard":
    print("test Passed")
else:
    print("test failed")
time.sleep(5)
driver.quit()
