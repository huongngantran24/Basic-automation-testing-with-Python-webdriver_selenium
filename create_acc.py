import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://store.steampowered.com/join/?&snr=1_60_4__62")

#enter email
email=driver.find_element(By.ID,'email')
email.send_keys("hoaanhdao2482000@gmail.com")
time.sleep(2)

#enter re-email
re_email=driver.find_element(By.ID,'reenter_email')
re_email.send_keys("hoaanhdao2482000@gmail.com")
time.sleep(2)

# select value in dropdown
chon = Select(driver.find_element(By.ID,'country'))
# select by visible text
chon.select_by_visible_text('Togo')
# select by value
chon.select_by_value('TG')
time.sleep(2)

#radio_btt= driver.find_element(By.CSS_SELECTOR,"input[value='roundtrip'")
#print("status of round trip radio button", radio_btt.is_selected()) #print status of radio button


select_ele=driver.find_element(By.NAME,"i_agree_check").click() #checkbox




