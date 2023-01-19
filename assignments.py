import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://inuvest.tech/")
driver.maximize_window()
driver.implicitly_wait(30)

'''                  LOGIN                         '''

""""           this is test case no.1                           """

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

""""           this is test case no.2                           """

driver.find_element(By.XPATH, "//*[@id='navbarBasicExample']/div[2]/div/div[2]/a[1]").click()
driver.find_element(By.XPATH, "//*[@id='first']/div[1]/div/input").send_keys("ENTER INVALID EMAIL")
driver.find_element(By.XPATH, "//*[@id='first']/div[2]/div/input").send_keys("ENTER INVALID PASSWORD")
driver.find_element(By.XPATH, "//*[@id='first']/div[3]/button").click()
Text = driver.find_element(By.XPATH, "//*[@id='swal2-title']").text

if Text == "Wrong username or password":
    print("test Passed")
else:
    print("test failed")
time.sleep(5)
driver.quit()

""""           this is test case no.3                           """

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

""""           this is test case no.4                           """

driver.find_element(By.XPATH, "//*[@id='navbarBasicExample']/div[2]/div/div[2]/a[1]").click()
driver.find_element(By.XPATH, "//*[@id='first']/div[1]/div/input").send_keys("VALID EMAIL")
driver.find_element(By.XPATH, "//*[@id='first']/div[2]/div/input").send_keys("INVALID PASSWORD")
driver.find_element(By.XPATH, "//*[@id='first']/div[3]/button").click()
Text = driver.find_element(By.XPATH, "//*[@id='swal2-title']").text

if Text == "Wrong username or password":
    print("test Passed")
else:
    print("test failed")
time.sleep(5)
driver.quit()

""""           this is test case no.5                           """

driver.find_element(By.XPATH, "//*[@id='navbarBasicExample']/div[2]/div/div[2]/a[1]").click()

driver.find_element(By.XPATH, "//*[@id='first']/div[3]/button").click()
Text = driver.find_element(By.XPATH, "//*[@id='swal2-title']").text

if Text == "Please enter all credentials" :
    print("test Passed")
else:
    print("test failed")
time.sleep(5)
driver.quit()

""""           this is test case no.6                           """

driver.find_element(By.XPATH, "//*[@id='navbarBasicExample']/div[2]/div/div[2]/a[1]").click()

driver.find_element(By.XPATH, "//*[@id='first']/div[3]/button").click()
Text = driver.find_element(By.XPATH, "//*[@id='swal2-title']").text

if Text == "Please enter all credentials":
    print("test Passed")
else:
    print("test failed")
time.sleep(5)
driver.quit()
#####################################################################################################################################################

"""                              SIGN UP TEST CASES                       """
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://inuvest.tech/")

driver.maximize_window()
driver.implicitly_wait(30)

""""           this is test case no.1                           """

driver.find_element(By.XPATH, "//*[@id='navbarBasicExample']/div[2]/div/div[2]/a[2]").click()
driver.find_element(By.XPATH, "//*[@id='first']/div[1]/div/input").send_keys("VALID NAME")
driver.find_element(By.XPATH, "//*[@id='first']/div[2]/div/input").send_keys("VALID LAST NAME")
driver.find_element(By.XPATH, "//*[@id='first']/div[3]/div/input").send_keys("VALID PHONE NUMBER")
driver.find_element(By.XPATH, "//*[@id='first']/div[4]/div/input").send_keys("VALID EMAIL ID")
driver.find_element(By.XPATH, "//*[@id='first']/div[5]/div/input").send_keys("VALID PASSWORD")
driver.find_element(By.XPATH, "//*[@id='first']/div[7]/button").click()
confirmation = driver.find_element(By.XPATH, "//*[@id='swal2-title']").text
if confirmation == "Confirmation email has been sent to your email address. Please confirm to continue.":
    print("test passed")
else:
    print("test failed")
driver.quit()

""""           this is test case no.2                           """

driver.find_element(By.XPATH, "//*[@id='navbarBasicExample']/div[2]/div/div[2]/a[2]").click()
driver.find_element(By.XPATH, "//*[@id='first']/div[1]/div/input").send_keys("SAME NAME")
driver.find_element(By.XPATH, "//*[@id='first']/div[2]/div/input").send_keys("SAME LAST NAME")
driver.find_element(By.XPATH, "//*[@id='first']/div[3]/div/input").send_keys("SAME PHONE NUMBER")
driver.find_element(By.XPATH, "//*[@id='first']/div[4]/div/input").send_keys("SAME EMAIL")
driver.find_element(By.XPATH, "//*[@id='first']/div[5]/div/input").send_keys("SAME PASSWORD")
driver.find_element(By.XPATH, "//*[@id='first']/div[7]/button").click()
confirmation = driver.find_element(By.XPATH, "//*[@id='swal2-title']").text
if confirmation == "This user already exists":
    print("test passed")
else:
    print("test failed")
driver.quit()

""""           this is test case no.3                           """

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

""""           this is test case no.4                           """

driver.find_element(By.XPATH, "//*[@id='navbarBasicExample']/div[2]/div/div[2]/a[2]").click()
driver.find_element(By.XPATH, "//*[@id='first']/div[1]/div/input").send_keys("VALID NAME")
driver.find_element(By.XPATH, "//*[@id='first']/div[2]/div/input").send_keys("VALID LAST NAME")
driver.find_element(By.XPATH, "//*[@id='first']/div[3]/div/input").send_keys("INVALID PHONE NUMBER") # here we will type alphabets
driver.find_element(By.XPATH, "//*[@id='first']/div[4]/div/input").send_keys("VALID EMAIL ID")
driver.find_element(By.XPATH, "//*[@id='first']/div[5]/div/input").send_keys("VALID PASSWORD")
driver.find_element(By.XPATH, "//*[@id='first']/div[7]/button").click()
confirmation = driver.find_element(By.XPATH, "//*[@id='swal2-title']").text
if confirmation == "Please enter correct number":
    print("test passed")
else:
    print("test failed")
driver.quit()

""""           this is test case no.5                           """

driver.find_element(By.XPATH, "//*[@id='navbarBasicExample']/div[2]/div/div[2]/a[2]").click()
driver.find_element(By.XPATH, "//*[@id='first']/div[1]/div/input").send_keys("VALID NAME")
driver.find_element(By.XPATH, "//*[@id='first']/div[2]/div/input").send_keys("VALID LAST NAME")
driver.find_element(By.XPATH, "//*[@id='first']/div[3]/div/input").send_keys("INVALID PHONE NUMBER")
driver.find_element(By.XPATH, "//*[@id='first']/div[4]/div/input").send_keys("VALID EMAIL ID")
driver.find_element(By.XPATH, "//*[@id='first']/div[5]/div/input").send_keys("VALID PASSWORD")
driver.find_element(By.XPATH, "//*[@id='first']/div[7]/button").click()
confirmation = driver.find_element(By.XPATH, "//*[@id='swal2-title']").text
if confirmation == "Please enter correct number":
    print("test passed")
else:
    print("test failed")
driver.quit()

""""           this is test case no.6                           """

driver.find_element(By.XPATH, "//*[@id='navbarBasicExample']/div[2]/div/div[2]/a[2]").click()
driver.find_element(By.XPATH, "//*[@id='first']/div[1]/div/input").send_keys("VALID NAME")
driver.find_element(By.XPATH, "//*[@id='first']/div[2]/div/input").send_keys("VALID LAST NAME")
driver.find_element(By.XPATH, "//*[@id='first']/div[3]/div/input").send_keys("VALID PHONE NUMBER")
driver.find_element(By.XPATH, "//*[@id='first']/div[4]/div/input").send_keys("VALID EMAIL ID")
driver.find_element(By.XPATH, "//*[@id='first']/div[5]/div/input").send_keys("INVALID PASSWORD")
driver.find_element(By.XPATH, "//*[@id='first']/div[7]/button").click()
confirmation = driver.find_element(By.XPATH, "//*[@id='swal2-title']").text
if confirmation == "Please enter correct password":
    print("test passed")
else:
    print("test failed")
driver.quit()


""""           this is test case no.7                           """


driver.find_element(By.XPATH, "//*[@id='navbarBasicExample']/div[2]/div/div[2]/a[2]").click()
driver.find_element(By.XPATH, "//*[@id='first']/div[1]/div/input").send_keys("INVALID NAME") # MEANS TYPE NUMBERS INSTEAD OF ALPHABETS
driver.find_element(By.XPATH, "//*[@id='first']/div[2]/div/input").send_keys("VALID LAST NAME")
driver.find_element(By.XPATH, "//*[@id='first']/div[3]/div/input").send_keys("VALID PHONE NUMBER")
driver.find_element(By.XPATH, "//*[@id='first']/div[4]/div/input").send_keys("VALID EMAIL ID")
driver.find_element(By.XPATH, "//*[@id='first']/div[5]/div/input").send_keys("VALID PASSWORD")
driver.find_element(By.XPATH, "//*[@id='first']/div[7]/button").click()
confirmation = driver.find_element(By.XPATH, "//*[@id='swal2-title']").text
if confirmation == "Please enter alphabets in Name":
    print("test passed")
else:
    print("test failed")
driver.quit()

'''                          this is test case no. 8'''
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


""""           this is test case no.9                           """

driver.find_element(By.XPATH, "//*[@id='navbarBasicExample']/div[2]/div/div[2]/a[2]").click()
driver.find_element(By.XPATH, "//*[@id='first']/div[7]/button").click()

confirmation = driver.find_element(By.XPATH, "//*[@id='swal2-title']").text
if confirmation == "Please fill all the credential before clicking on the sifn up":
    print("test passed")
else:
    print("test failed")
driver.quit()


""""           this is test case no.10                          """


driver.find_element(By.XPATH, "//*[@id='navbarBasicExample']/div[2]/div/div[2]/a[2]").click()
driver.find_element(By.XPATH, "//*[@id='first']/div[1]/div/input").send_keys("VALID NAME")
driver.find_element(By.XPATH, "//*[@id='first']/div[3]/div/input").send_keys("VALID PHONE NUMBER")
driver.find_element(By.XPATH, "//*[@id='first']/div[4]/div/input").send_keys("VALID EMAIL ID")
driver.find_element(By.XPATH, "//*[@id='first']/div[5]/div/input").send_keys("VALID PASSWORD")
driver.find_element(By.XPATH, "//*[@id='first']/div[7]/button").click()
confirmation = driver.find_element(By.XPATH, "//*[@id='swal2-title']").text
if confirmation == "Please fill all the mandatory fields":
    print("test passed")
else:
    print("test failed")
driver.quit()

'''                              SCROLL                      '''

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
