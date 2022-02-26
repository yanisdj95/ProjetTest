import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from flask import request

browser = webdriver.Chrome("C:\\Users\\yanis\Downloads\\chromedrivertest\\chromedriver_win32\\chromedriver.exe")

browser.get('https://www.zalando.fr/release-calendar/homme-sneakers/')

browser.maximize_window()
time.sleep(1.7)
cookies = browser.find_element_by_xpath('//*[@id="uc-btn-accept-banner"]')
cookies.click()

paires_prix = browser.find_elements_by_class_name('A95iT1 pDVUjz nmA88J NNECXo AHAcbe EIxEFh')
paires_marque = browser.find_elements_by_class_name('A95iT1 pDVUjz nmA88J RYaIlf AHAcbe minions-text-ellipsis')
paires_modele = browser.find_elements_by_class_name('A95iT1 pDVUjz nmA88J RYaIlf AHAcbe minions-text-ellipsis UySA7R')

request.post('http://127.0.0.1:5000/post', json = {"id": 1, "marque" : paires_marque[1].text, "modele" : paires_modele[1].text, "prix" : paires_prix[1].text})
"""for i in range(len(paires_prix)):"""
    
    
time.sleep(2)
browser.close()




