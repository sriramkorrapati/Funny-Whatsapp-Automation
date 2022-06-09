import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import pyautogui as pag


def userinputs():
    try:
        global name, limit, msg
        name = input("Enter Contact Name:")
        limit = int(input("Count: "))
        msg = input("Message: ")
    except:
        print("Unexpected Error in Receiving Data")


def callbrowser():
    try:
        global driver
        driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.get("https://web.whatsapp.com")
        driver.implicitly_wait(1000)
        # time.sleep(20)
    except:
        print("Driver Problem")


def callsearchbar():
    try:
        element = driver.find_element_by_class_name("_28-cz").click()
        time.sleep(1)
        pag.typewrite(name)
        time.sleep(1)
        pag.press('Enter')
        time.sleep(2)
    except:
        print("search bar problem")


def messagelooping():
    try:
        message = driver.find_element_by_class_name("p3_M1").click()
        i = 0
        driver.implicitly_wait(5)
        while i < int(limit):
            pag.typewrite(msg)
            pag.press('Enter')
            i += 1
        time.sleep(10)
    except:
        print("Message Sending Problem")


userinputs()
callbrowser()
callsearchbar()
messagelooping()


driver.close()

# Developed By "Sriram_Korrapati"
