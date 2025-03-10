import time

import py
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://automationplayground.com/crm/login.html")
time.sleep(5)

#driver.find_element(By.ID, "email-id").send_keys("confixhub@yopmail.com")
#time.sleep(5)
#driver.find_element(By.ID, "password").send_keys("Debbie19")
#time.sleep(5)
#driver.find_element(By.ID, "remember").click()
#time.sleep(5)
#driver.find_element(By.ID, "submit-name").click()
#time.sleep(5)


