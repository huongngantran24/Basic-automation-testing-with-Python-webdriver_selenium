##---------GET-------------
from selenium import webdriver
from  selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://chromedriver.chromium.org/")

print(driver.title) #print out the title of page
print(driver.current_url)
#print(driver.page_source)

driver.close()   #close the browser