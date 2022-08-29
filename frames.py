import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
#driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

driver.switch_to.frame('packageListFrame')#first frame
driver.find_element(By.LINK_TEXT,'org.openqa.selenium.chrome').click()
time.sleep(1)

driver.switch_to.default_content()

driver.switch_to.frame('packageFrame')#second frame
driver.find_element(By.LINK_TEXT,'ChromeDriver').click()
time.sleep(1)

#FAIL THIRD FRAME
driver.switch_to.frame('classFrame')#third frame
driver.find_element(By.XPATH,'/html/body/div[1]/ul/li[6]').click()
time.sleep(2)


