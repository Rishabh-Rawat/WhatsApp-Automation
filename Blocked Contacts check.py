from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def blocked_contacts():
    driver=webdriver.Chrome("chromedriver")
    driver.get("https://web.whatsapp.com/")

    element=WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="side"]/header/div[2]/div/span/div[3]/div/span')))
    element.click()

    element=WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[5]/div')))
    element.click()

    element=WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[4]/div[2]/div/span')))
    element.click()
    time.sleep(0.5)
    
    i=0
    L=[]

    while True:
        try:
            i=i+1
            xpath='//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div[1]/div[1]/div/div[{}]/div/div/div[2]/div[1]/div/span/span'.format(i)
            phno=driver.find_element_by_xpath(xpath).text
            L.append(phno)
        except:
            break

    driver.quit()
    
    contacts_list=[]
    for i in L:
        i=i.replace(" ","")
        i=i.strip("+")
        if i[0:2] == '91':
            contacts_list.append(i)
        
    return contacts_list


#__main__

blocked_contacts_list=blocked_contacts()

with open("Unique_Contacts.txt",'r') as f1:
    contacts_list=f1.readlines()
    
f2=open("Ready_to_use_Contacts.txt",'w')

L=[]
for i in contacts_list:
    i=i.strip('\n')
    if i not in blocked_contacts_list:
        f2.write(i+'\n')
     
    
f2.close()
print("The blocked contacts have been successully removed and final contacts are moved to 'Ready_to_use_Contacts' in your current directory")
        
        