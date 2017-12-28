# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from pyvirtualdisplay import Display
import requests
import sys

import unittest, time, re

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(5)
base_url = "file:///Users/lld/excel.htm"
verificationErrors = []
accept_next_alert = True
    
delay = 3
    
driver.get(base_url)
html_source = driver.page_source
data = html_source.encode('utf-8')
    
text = "instagram"
elements = driver.find_elements_by_xpath("//*[contains(text(), '"+text+"')]")
accounts_temp = []
accounts = []

for element in elements:
    temp = element.get_attribute("innerText")
    accounts_temp.append(temp.split("https://www.instagram.com")[1])

for account in accounts_temp:
    accounts.append(account.strip())

driver.quit()

print "_______________________________________________"
print "_____________ALL ACCOUNTS FOUND(Instagram)_____"
print "_______________________________________________"

howmany = len(accounts)
status = 0
message = ""
url = "https://api.telegram.org/bot489531889:AAHwSgHDxQ6vx9UKSXvB86d10my4X_mNliA/"

def send_mess(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

for account in accounts:

    driver = webdriver.Chrome('./chromedriver')
    driver.implicitly_wait(5)
    base_url = "http://picbear.com"
    verificationErrors = []
    accept_next_alert = True

    delay = 3
        
    driver.get(base_url + account)
    for i in range(1,7):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
    html_source = driver.page_source
    data = html_source.encode('utf-8')
            
    found = 0
            
    texts = ['Выборы Президента','По итогам 2017','подведены итоги года','была модернизирована система','подвел основные итоги','В этом году хорошо']
                
    for text in texts:
        el = driver.find_elements_by_xpath("//*[contains(text(), '"+text+"')]")
        if (len(el) > 0):
            found += 1

    status += 1
    print str(status) + "/" + str(howmany) + ") " + str(account) + " - " + str(found)
    message = message + str(status) + "/" + str(howmany) + ") " + str(account) + " - " + str(found) + "\n"
    driver.quit()

texts_string = ", ".join(texts)
send_mess(162813337, "INSTAGRAM INSTAGRAM INSTAGRAM INSTAGRAM INSTAGRAM INSTAGRAM INSTAGRAM \n\n"+ "C НАСТУПАЮЩИМ ВИК xDDDD Новость про вот эту хуйню: " + texts_string + "\n\n" + message)

