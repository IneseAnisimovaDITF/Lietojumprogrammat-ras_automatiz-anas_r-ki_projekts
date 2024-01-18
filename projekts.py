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

url = "https://id2.rtu.lv/openam/UI/Login?module=LDAP&locale=lv" # adrese ar lapu kuru mes velamies atvert
driver.get(url)
time.sleep(2)

piekritu=driver.find_element(By.ID,"cn-notice-button-aggree")
piekritu.click()
time.sleep(2)

lietotajs=driver.find_element(By.CLASS_NAME, "TxtFld")
lietotajs.send_keys("inese.anisimova")

parole=driver.find_element(By.ID, "IDToken2")
parole.send_keys("tejabutistaparole")

pieteikties=driver.find_element(By.NAME, "Login.Submit")
pieteikties.click()
time.sleep(2)

studentiem=driver.find_element(By.XPATH, '//li[@class=""]/a[@title="Studentiem"]')
studentiem.click()

estudijas=driver.find_element(By.XPATH, '//a[text()="Atvērt e-studiju sistēmu"]')
estudijas.click()

time.sleep(3)
infopanelisgaidamienot=driver.find_element(By.CLASS_NAME, "pb-2")
print(infopanelisgaidamienot.text)

izvade = "izvade.txt"
eksamgraf = "eksamgraf.txt"

with open(izvade, 'w', encoding='utf-8') as output_file:
    output_file.write(infopanelisgaidamienot.text)

username = "macibas.projekts@gmail.com"
password = "byedbgkbjerjyqeb"

gmail_server = "smtp.gmail.com"
gmail_port = 587

serveris = smtplib.SMTP(gmail_server, gmail_port)
serveris.ehlo()
serveris.starttls()

serveris.login(username, password)

rinduskaititajs = ""
failusaglaba = "izvade.txt"
with open(failusaglaba, "r", encoding="utf-8") as file:
    for i, line in enumerate(file, start=1):
        if i not in {4, 5, 9, 10, 14, 15, 19, 20, 24, 25, 29, 30, 34, 35, 39, 40, 44, 45, 49, 50, 54, 55, 59, 60, 64, 65, 69, 70}:
            tuksizlaizam = line.strip()
            rinduskaititajs += tuksizlaizam + "\n"

msg = EmailMessage()
msg.set_content("Labdien Jums ir jāizpilda uzdevumus ↓" + "\n" + failusaglaba + "\n" + "Veiksmi darbā!" + "\n" + "Ar cieņu, Jūsu gmail konts")

msg["Subject"] = ""
msg["From"] = username
msg["To"] = username

serveris.send_message(msg)

serveris.quit()

