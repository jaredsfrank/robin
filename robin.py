from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import calendar
import time


username = 'PutYourUserNameHere'
password = 'PutYourPasswrdHere'
timeout = 4

def run():
    driver = webdriver.Firefox()
    driver.get("http://www.reddit.com/robin")
    usr = driver.find_element_by_id("user_login")
    passwrd = driver.find_element_by_id("passwd_login")
    usr.send_keys(username)
    passwrd.send_keys(password)
    driver.find_elements_by_class_name("c-btn")[1].click()
    start = calendar.timegm(time.gmtime())
    while calendar.timegm(time.gmtime()) - start < timeout:
        try:
            driver.find_elements_by_class_name("robin-chat--vote")[2].click()
            break
        except:
            continue
    driver.quit()

while True:      
    run()


