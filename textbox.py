import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
#driver.refresh()
#how to find how many inputboxes present in web page
#inputboxes=driver.find_elements(By.CLASS_NAME,"text_field")
#print(len(inputboxes)) #6

#how to  know status
#status=driver.find_element(By.ID,"RESULT_TextField-1").is_displayed()
#print(status)  #true/false

#how to provide value into textbox
#driver.find_element(By.ID,"RESULT_TextField-1").send_keys("Hương ngân")
#time.sleep(2)
#driver.find_element(By.ID,"RESULT_TextField-2").send_keys("TRẦN THỊ")
#time.sleep(2)
#driver.find_element(By.ID,"RESULT_TextField-3").send_keys("5467887654345678")
#time.sleep(2)
#driver.find_element(By.ID,"RESULT_TextField-4").send_keys("VIET NAM")
#time.sleep(2)
#driver.find_element(By.ID,"RESULT_TextField-5").send_keys("ĐÀ NẴNG")
#time.sleep(2)
#driver.find_element(By.ID,"RESULT_TextField-6").send_keys("VMSF0978S9S")

radio_btt=driver.find_element(By.XPATH,"//label[contains(text(),'Female')]").click()

checkbox_btt=driver.find_element(By.XPATH,"//label[contains(text(),'Sunday')]").click()
checkbox_btt2=driver.find_element(By.XPATH,"//label[contains(text(),'Monday')]").click()



#driver.close()   #close the browser