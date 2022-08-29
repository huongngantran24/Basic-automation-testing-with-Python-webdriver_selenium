import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://phunutoday.vn/")

links=driver.find_elements(By.TAG_NAME,"a")

print("Number of links present: ",len(links))
time.sleep(2)
#for link in links:
#   print(link.text)

#click on tab link
#driver.find_element(By.LINK_TEXT,'THỜI TRANG').click()

