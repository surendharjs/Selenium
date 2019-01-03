import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("http://172.17.12.50/CodelogixTest")
elem1 = driver.find_element_by_xpath('//*[@id="user"]')
elem1.send_keys("Superadmin")

elem1 = driver.find_element_by_xpath('//*[@id="pw"]')
elem1.send_keys("Welcome@123")
elem1 = driver.find_element_by_xpath('//*[@id="checkUsrLogin"]')
elem1.click()

time.sleep (5)

driver.close()




