import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_contacts():
    name=input("Enter exact name of group : ")
    group_xpath = '//span[@title = "{}"]'.format(name)

    driver=webdriver.Chrome("chromedriver")
    driver.get("https://web.whatsapp.com/")

    element=WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH,group_xpath)))
    element.click()

    time.sleep(2)
    contacts=driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[2]/span').text.split(',')
    driver.quit()

    phno=[]
    for i in contacts:
        if i[0:4]==" +91":
            i=i.replace(" ","")
            i=i.lstrip(" +")
            phno.append(i)

    f=open("All_Contacts.txt","a")
    for j in phno:
        f.write(j+"\n")
    
    print("The contacts from this group have been successfully moved to 'All_Contacts' in your current directory")
    f.close()

#__main__
get_contacts()
