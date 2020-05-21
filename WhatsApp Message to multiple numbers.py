import time
import pyautogui as py
from selenium import webdriver

def give_open_whatsapp_position():
    '''This function returns the position of the OpenWhatsApp button on the screen
        as per the current monitor resolution'''
    size_of_screen=py.size()           # stores the current resolution of the monitor
    if size_of_screen==(1280,960):                                               
        open_whatsapp_position=(711,187)  # button position for screen with resolution 1280x960
    elif size_of_screen==(1280,720) or size_of_screen==(1280,600):               
        open_whatsapp_position=(703,184) #button position for resolution 1280x720 or 1280x600
    elif size_of_screen==(800,600):                                              
        open_whatsapp_position=(475,188)    # button position for screen with resolution 800x600
    else:                # calculating position for all other valid screen resolutions
        total_x_size=size_of_screen[0]
        total_y_size=size_of_screen[1]
        open_whatsapp_x_coordinate=(55/100)*total_x_size
        open_whatsapp_y_coordinate=(22.75/100)*total_y_size
        open_whatsapp_position=(open_whatsapp_x_coordinate,open_whatsapp_y_coordinate)
    return open_whatsapp_position        # returns the required position of the button

def screen_available():
    while True:
        if py.locateOnScreen("Detect.png"):
            return True
    
def two_lines():
    py.hotkey('shift','enter')
    py.hotkey('shift','enter')
        
with open("Contacts2.txt","r") as f1:
    contacts=f1.readlines()

c=0
for phno in contacts:
    phno=phno.strip()
    driver=webdriver.Chrome("chromedriver")
    driver.get("https://wa.me/"+phno)

    driver.maximize_window()
    time.sleep(0.5)

    required_position=give_open_whatsapp_position()
    py.click(required_position)
    time.sleep(1)
    
    if screen_available():
        
        py.typewrite('*PUBG MOBILE SQUAD TOURNAMENT*')
        two_lines()
        py.typewrite('*DATE:- 23/05/2020  SATURDAY*')
        two_lines()
        py.typewrite('*TIME:- 11:50 PM (NIGHT)*')
        two_lines()
        py.typewrite('*SQUAD ERANGEL*')
        two_lines()
        py.typewrite('*PRIZE:*')
        py.hotkey('shift','enter')
        py.typewrite('*Rs.10 PER KILL*')
        py.hotkey('shift','enter')
        py.typewrite('*Rs.20 EXTRA FOR CHICKEN DINNER*')
        two_lines()
        py.typewrite('*ENTRY FEES:-Rs.10 per player*')
        two_lines()
        py.typewrite('*Full details:*')
        py.hotkey('shift','enter')
        py.typewrite('https://www.toornament.com/en_GB/tournaments/3415329751851745280/information')
        two_lines()
        py.typewrite('*Registration:*')
        py.hotkey('shift','enter')
        py.typewrite('SEND THE *TEAM DETAILS ALONG WITH ENTRY FEE PAYMENT SCREENSHOT* TO https://wa.me/919410576788 IN THE FOLLOWING FORMAT. ')
        two_lines()
        py.typewrite('*TEAM NAME:*')
        py.hotkey('shift','enter')
        py.typewrite('*PLAYER 1:*')
        py.hotkey('shift','enter')
        py.typewrite('*PLAYER 2:*')
        py.hotkey('shift','enter')
        py.typewrite('*PLAYER 3:*')
        py.hotkey('shift','enter')
        py.typewrite('*PLAYER 4:*')
        two_lines()
        py.typewrite('*NO EMULATORS*')
        two_lines()
        py.typewrite('*FOR MORE TOURNAMENTS JOIN:*')
        py.hotkey('shift','enter')
        py.typewrite('https://chat.whatsapp.com/Jq1VZDFVRI8KxBaGP9affJ')
        two_lines()
        py.typewrite('*For Queries:*')
        py.hotkey('shift','enter')
        py.typewrite('1. https://wa.me/919410576788')
        py.hotkey('shift','enter')
        py.typewrite('2. https://wa.me/917617409819')
        
        time.sleep(5)
        py.press('enter')
    
    c=c+1
    print(c,"messages sent")
    py.click(1904,4)
    driver.quit()
