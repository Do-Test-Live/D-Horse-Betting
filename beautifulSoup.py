from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://bet.hkjc.com/racing/pages/odds_wpq.aspx?lang=en&raceno=1")
time.sleep(5)

rows = driver.find_element(By.XPATH, '//*[@id="container"]/div/div/div[2]/div[2]').get_attribute("outerHTML")

# Create a BeautifulSoup object and specify the parser
soup = BeautifulSoup(rows, 'html.parser')

# Find the parent <div> element
parent_div = soup.find('div', class_='racebg')

# Find all <div> child elements inside the parent <div>
child_divs = parent_div.find_all('div')

# Count the total number of <div> child elements
total_child_divs = len(child_divs)

j=1

while j<total_child_divs-1:

    driver.get("https://bet.hkjc.com/racing/pages/odds_wpq.aspx?lang=en&raceno="+str(j))
    time.sleep(2)

    rows = driver.find_elements(By.XPATH, '//*[@id="wpt'+str(j)+'"]/table/tbody/tr')

    i = 1
    for data in rows:
        i = i + 1

    print('Race '+str(j)+' : rows '+str(i))

    x = 1

    while x<i-1:
        sl = driver.find_element(By.XPATH, '//*[@id="wpt'+str(j)+'"]/table/tbody/tr[' + str(x) + ']/td[1]').text
        horsename = driver.find_element(By.XPATH, '//*[@id="wpt'+str(j)+'"]/table/tbody/tr[' + str(x) + ']/td[4]').text
        win = driver.find_element(By.XPATH, '//*[@id="wpt'+str(j)+'"]/table/tbody/tr[' + str(x) + ']/td[5]').text
        place = driver.find_element(By.XPATH, '//*[@id="wpt'+str(j)+'"]/table/tbody/tr[' + str(x) + ']/td[6]').text

        print('Win: '+win+' Place: '+place)
        x=x+1

    j=j+1

    print('\n\n')