import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
#driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH,"//*[@id='HTML9']/div[1]/button").click()
time.sleep(1)
driver.switch_to.alert.accept()
#driver.switch_to.alert.dismiss()

