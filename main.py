from bs4 import BeautifulSoup
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import csv
import requests
import time

driver = webdriver.Chrome()
driver.maximize_window()


j=1

while j<8:

    driver.get("https://bet.hkjc.com/racing/pages/odds_wpq.aspx?lang=en&date=2023-06-22&venue=S1&raceno="+str(j))
    time.sleep(5)

    rows = driver.find_elements(By.XPATH, '//*[@id="wpt'+str(j)+'"]/table/tbody/tr')

    i = 1
    for data in rows:
        i = i + 1

    print(i)

    fields = ['SL', "Horsename", 'Win', 'Place']
    with open(r'Output/Race'+str(j)+'.csv', 'a', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(fields)

    x = 1

    while x<i-1:
        sl = driver.find_element(By.XPATH, '//*[@id="wpt'+str(j)+'"]/table/tbody/tr[' + str(x) + ']/td[1]').text
        horsename = driver.find_element(By.XPATH, '//*[@id="wpt'+str(j)+'"]/table/tbody/tr[' + str(x) + ']/td[4]').text
        win = driver.find_element(By.XPATH, '//*[@id="wpt'+str(j)+'"]/table/tbody/tr[' + str(x) + ']/td[5]').text
        place = driver.find_element(By.XPATH, '//*[@id="wpt'+str(j)+'"]/table/tbody/tr[' + str(x) + ']/td[6]').text

        x=x+1

        fields = [sl, horsename, win, place]
        with open(r'Output/Race'+str(j)+'.csv', 'a', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(fields)

    j=j+1