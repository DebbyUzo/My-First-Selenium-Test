import time

import py
from selenium import webdriver
from selenium.webdriver.common.by import By

#this is initiating chrome
driver = webdriver.Chrome()

#to nagivate to the login page of automation playground
driver.get("https://automationplayground.com/crm/login.html")
time.sleep(5)

#Login with email address
driver.find_element(By.ID, "email-id").send_keys("confixhub@yopmail.com")
time.sleep(5)

#input valid password
driver.find_element(By.ID, "password").send_keys("Debbie19")
time.sleep(5)

#Click remember Me
driver.find_element(By.ID, "remember").click()
time.sleep(5)

#Click Submit button
driver.find_element(By.ID, "submit-name").click()
time.sleep(5)

#Click on new customers
driver.find_element(By.ID, "new-customer").click()
time.sleep(5)

#input valid emailaddress
driver.find_element(By.ID, "EmailAddress").send_keys("confixhub@yopmail.co")
time.sleep(5)

#Enter Firstname
driver.find_element(By.ID, "FirstName").send_keys("Debbie")
time.sleep(5)

#Enter Lastname
driver.find_element(By.ID, "LastName").send_keys("Agomuo")
time.sleep(5)

#Enter City
driver.find_element(By.ID, "City").send_keys("Okota")
time.sleep(5)

#Select State
driver.find_element(By.ID, "StateOrRegion").send_keys("Lagos")
time.sleep(5)

#Select gender
driver.find_element(By.ID, "gender").send_keys("female")
time.sleep(5)

#click add to promotional list
driver.find_element(By.ID, " Add to promotional list").click()
time.sleep(5)

#click submit button
driver.find_element(By.ID, "submit").click()
time.sleep(5)

#Click sign out button
driver.find_element(By.ID, "Sign Out").click()
time.sleep(5)