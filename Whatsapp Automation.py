from selenium import webdriver
import pyautogui as pag


name = input("Enter Contact Name: ")
limit = int(input("Count: "))
msg = input("Message: ")

driver = webdriver.Chrome(executable_path="/Applications/chromedriver")
driver.maximize_window()
driver.get("https://web.whatsapp.com")
driver.implicitly_wait(120)

driver.find_element_by_xpath('//span[@title = "{}"]'.format(name)).click();
driver.find_element_by_class_name("p3_M1").click();

i = 0
driver.implicitly_wait(5)
while i < int(limit):
    pag.typewrite(msg)
    pag.press('Enter')
    i += 1

input("Press Enter To Exit")
