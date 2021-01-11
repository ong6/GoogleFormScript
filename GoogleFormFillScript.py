
# This can be used to autofill any google form
# Replace the x_p_values with the xpath of the form items

import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# change this is the directory that chromedriver is installed in
chromedriver = "..."
driver = webdriver.Chrome(chromedriver)


# change this to the link to the form
link = ' ...'
driver.get(link)

x_p_name = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
x_p_tele = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
x_p_exp = '//*[@id="i13"]/div[3]'
x_p_gar = '//*[@id="i26"]/div[3]'
x_p_wait = '//*[@id="i39"]/div[3]'

submit_xp = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span'

count = 1

# d1 and f2 are for word fields, the rest are for selection fields.


def fill_form(field1, field2):
    d1 = driver.find_element_by_xpath(x_p_name)
    d1.send_keys(field1)
    # time.sleep(0.01)
    d2 = driver.find_element_by_xpath(x_p_tele)
    d2.send_keys(field2)
    # time.sleep(0.01)
    d3 = driver.find_element_by_xpath(x_p_exp)
    d3.click()
    # time.sleep(0.01)
    d4 = driver.find_element_by_xpath(x_p_gar)
    d4.click()
    # time.sleep(0.01)
    d5 = driver.find_element_by_xpath(x_p_wait)
    d5.click()
    # time.sleep(0.01)
    submit = driver.find_element_by_xpath(submit_xp)
    submit.click()
    driver.get(link)
