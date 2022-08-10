import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://dangnhap.thanhhoa.gov.vn/login")

user_ele=driver.find_element("xpath","//*[@id='username']")
print(user_ele.is_displayed()) #return true/false based of element status
user_ele.is_enabled()#return true/false

pass_ele=driver.find_element("xpath","//*[@id='password']")
print(pass_ele.is_displayed()) #return true/false based of element status
pass_ele.is_enabled()#return true/false

user_ele.send_keys("huong ngan")
time.sleep(3)
pass_ele.send_keys("huongngan142534")
time.sleep(3)

login_button=driver.find_element("xpath","//*[@id='fm1']/section[2]/div[2]/input").click()

driver.close()


