import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import smtplib 
from email.message import EmailMessage

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)
# webdriver.Chrome(service=service, options=option)

url="https://id2.rtu.lv/openam/UI/Login?module=LDAP&locale=lv"
driver.get(url)
time.sleep(2)

# piekritu=driver.find_element(By,ID, "cn-notice-button-aggree")
# piekritu.click()
# time.sleep(2)

input()

# izvade = "izvade.txt"
