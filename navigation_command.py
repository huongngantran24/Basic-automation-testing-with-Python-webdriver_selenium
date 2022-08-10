#------switch between visited sites--------
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://translate.google.com/?hl=vi")
print(driver.title)

driver.get("https://demo.automationtesting.in/Windows.html")
time.sleep(5)
print(driver.title)

driver.back()
time.sleep(5)
print(driver.title)

driver.forward()
time.sleep(5)
print(driver.title)

driver.quit()
