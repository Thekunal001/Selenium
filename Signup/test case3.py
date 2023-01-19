# IN THIS TEST CASE OUR WEBSITE IS PROVIDING THIS POP UP OF INVALID PHONE NUMBER AND EMAIL NUMBER BUT WE CAN ADD THESE POP UPS AND AFTER ADDING THAT WE CAN CHECK THEM THROUGH THE if CONDITION THAT I HAVE USED AT THE LAST IN TEST CASE 3, 4, 5, 6, 7 and 8

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
driver.find_element(By.XPATH, "//*[@id='first']/div[2]/div/input").send_keys("VALID LAST NAME")
driver.find_element(By.XPATH, "//*[@id='first']/div[3]/div/input").send_keys("VALID PHONE NUMBER")
driver.find_element(By.XPATH, "//*[@id='first']/div[4]/div/input").send_keys("INVALID EMAIL ID")
driver.find_element(By.XPATH, "//*[@id='first']/div[5]/div/input").send_keys("VALID PASSWORD")
driver.find_element(By.XPATH, "//*[@id='first']/div[7]/button").click()
confirmation = driver.find_element(By.XPATH, "//*[@id='swal2-title']").text
if confirmation == "Please enter correct email id":
    print("test passed")
else:
    print("test failed")
driver.quit()
