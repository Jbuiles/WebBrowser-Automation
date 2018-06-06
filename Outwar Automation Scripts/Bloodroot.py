import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

options = Options()
options.set_headless(headless=True)
//User Input
Accountsfull = {''}
yourlogin = 'yourlogin'
yourpassword = 'yourpassword'
yourserver = 'yourserver'

link ='https://'+yourserver+'.outwar.com/world?suid='

//HTML Locations
Form= 'body > center:nth-child(20) > div:nth-child(1) > div:nth-child(3) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(3) > form:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > div:nth-child(1) > input:nth-child(10)'
Raid= '#roomDetails > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(3) > a:nth-child(1) > img:nth-child(1)'
Join= 'body > center:nth-child(20) > div:nth-child(1) > div:nth-child(3) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(5) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(3) > form:nth-child(6) > input:nth-child(2)'
Launch= 'body > center:nth-child(20) > div:nth-child(1) > div:nth-child(3) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(5) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > div:nth-child(3) > form:nth-child(1) > input:nth-child(3)'

def init_driver():
    browser = webdriver.Firefox(firefox_options=options, executable_path=r'C:\Users\YOURUSER\AppData\Local\Programs\Python\Python36-32\geckodriver.exe')
    browser.wait = WebDriverWait(browser, 10)
    return browser

def login():
	browser.get('https://'+yourserver+'.outwar.com/login')
	user = browser.find_element_by_name('login_username')
	password = browser.find_element_by_name('login_password')
	user.send_keys(yourlogin)
	password.send_keys(yourpassword)
	submit = browser.find_element_by_name('submitit')
	submit.submit()
	print('Successful Login')
	time.sleep(2)
	
def formraid():
	browser.get('https://'+yourserver+'.outwar.com/world?suid=')#Your Raid Former
	try:
		button1 = browser.wait.until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'Raid')))
		button1.click()
		button2 = browser.wait.until(EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'Form')))
		button2.click()
		print('Successful Form')
		
	except TimeoutException:
		print("Raid not up")
		browser.close()

def joinraid():
        try:
                for k, v in Accountsfull.items():
                        browser.get(link+k)
                        raidbutton = browser.wait.until(EC.presence_of_element_located(
                                (By.CSS_SELECTOR, 'Raid')))
                        raidbutton.click()
                        joinraid = browser.wait.until(EC.element_to_be_clickable(
                                (By.CSS_SELECTOR, 'Join')))
                        joinraid.click()
                        print(v + " Joined")
        except TimeoutException:
            print("Not in room")
            browser.close()
        print('Successful Join')

def launchraid():
	browser.get('https://'+yourserver+'.outwar.com/world?suid=')#Your Raid Former
	try:
		raid = browser.wait.until(EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'Raid')))
		raid.click()
		launchraid = browser.wait.until(EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'Launch')))
		launchraid.click()
		print('Successful Launch')
		
	except TimeoutException:
		print("Can't Launch")
		browser.close()
		
browser = init_driver()
login()
formraid()
joinraid()
launchraid()
browser.close()
