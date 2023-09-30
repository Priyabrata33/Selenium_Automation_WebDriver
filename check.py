from typing import List
from selenium import webdriver
import time
import csv

driver = webdriver.Chrome()
driver.get("http://result23.msbuexam.in/(S(it50ynziv2ofn03dnvqsyc1m))/Result/BEdResult.aspx")



list = [[]]

for i in range(515351,515444):

    text_area = driver.find_element('xpath','//*[@id="txtfromNo"]')
    text_area.send_keys(i)
    time.sleep(1)
    sumb = driver.find_element('xpath', '//*[@id="btnSave"]')
    sumb.click()


   
    inList = []

    
    #name
    for element in driver.find_elements('xpath','//*[@id="form1"]/div[3]/div[2]/table/tbody/tr[5]/td/table/tbody/tr[1]/td[2]'):
     inList.append(element.text)

    #father's_Name
    for element in driver.find_elements('xpath','//*[@id="form1"]/div[3]/div[2]/table/tbody/tr[5]/td/table/tbody/tr[3]/td[2]'):
        inList.append(element.text)

    #Roll_Name
    for element in driver.find_elements('xpath','//*[@id="form1"]/div[3]/div[2]/table/tbody/tr[5]/td/table/tbody/tr[2]/td[2]'):
        inList.append(element.text)

    #EnrollMentNumber
    for element in driver.find_elements('xpath','//*[@id="form1"]/div[3]/div[2]/table/tbody/tr[5]/td/table/tbody/tr[5]/td[2]'):
        inList.append(element.text)

    #part1
    for element in driver.find_elements('xpath','//*[@id="form1"]/div[3]/div[2]/table/tbody/tr[10]/td/table/tbody/tr[1]/td[2]'):
        inList.append(element.text)

    #part2
    for element in driver.find_elements('xpath','//*[@id="form1"]/div[3]/div[2]/table/tbody/tr[10]/td/table/tbody/tr[2]/td[2]'):
        inList.append(element.text)

    #total
    for element in driver.find_elements('xpath','//*[@id="form1"]/div[3]/div[2]/table/tbody/tr[10]/td/table/tbody/tr[3]/td[2]'):
        inList.append(element.text)

    #divisions
    for element in driver.find_elements('xpath','//*[@id="form1"]/div[3]/div[2]/table/tbody/tr[10]/td/table/tbody/tr[4]/td[2]'):
        inList.append(element.text)

    # adding to list of lists    
    list.append(inList)

    driver.back()
    text_area.clear()


# print(list)


with open('out.csv', 'w', newline='') as f:
    writer = csv.writer(f,delimiter='|')
    writer.writerows(list)

driver.quit()




# selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id="txtfromNo"]"}
#   (Session info: chrome=117.0.5938.92); For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors#no-such-element-exception