# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 17:26:21 2020

@author: alber
"""


import time
import os
from tqdm import tqdm
from tqdm import trange
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import io


url = "https://www.facebook.com/"

url2 = "https://www.facebook.com/DummyGroup/photos/g.453831641445861/3107314719338346/?type=1&theater&ifg=1"
user = "mail@mail.com"
password = "Password"

def	login(user, password):
    usr = driver.find_element_by_name("email")		
    usr.send_keys(user)
    passw = driver.find_element_by_name("pass")		
    passw.send_keys(password)
    driver.find_element_by_name("pass").send_keys(Keys.ENTER)  

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(url)

login(user, password)
time.sleep(5)



#### Step 2
driver.get(url2)
time.sleep(5)

for i in trange(1000):
    with open(str(i) + '.png', 'wb') as file:
        image = driver.find_element_by_class_name('spotlight')

        file.write(image.screenshot_as_png)
        alt = image.get_attribute("alt")
        alt = alt.replace("La imagen puede contener: texto que dice ", "" )

        # print(alt)

        
        with io.open(str(i) + '.txt', "w", encoding="utf-8") as f:
            f.write(alt)
            f.close() #This close() is important

        
        driver.find_element_by_css_selector('body').send_keys(Keys.RIGHT)  
        time.sleep(1)


