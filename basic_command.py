#--------Click button by find Xpath--------
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://demo.automationtesting.in/Windows.html")

print(driver.title)
print(driver.current_url)

driver.find_element("xpath","//*[@id='Tabbed']/a/button").click() #Click on button "CLICK"

time.sleep(5)
#driver.close()#close currenttly focussed browser
driver.quit() #close all tab of browser