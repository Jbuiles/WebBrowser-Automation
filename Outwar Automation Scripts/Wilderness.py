import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
options.set_headless(headless=True)

//User Input
yourlogin = 'yourlogin'
yourpassword = 'yourpassword'
yourserver = 'yourserver'
yourid = 'yourcharacterid'

//HTML Locations
Wilderness= 'body > center:nth-child(20) > div:nth-child(1) > div:nth-child(3) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > center:nth-child(5) > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(3) > a:nth-child(4) > img:nth-child(1)'

def init_driver():
    browser = webdriver.Firefox(firefox_options=options, executable_path=r'C:\Users\YOURUSER\AppData\Local\Programs\Python\Python36-32\geckodriver.exe')
    browser.wait = WebDriverWait(browser, 10)
    return browser

def login():
	browser.get('https://+yourserver+.outwar.com/login')
	user = browser.find_element_by_name('login_username')
	password = browser.find_element_by_name('login_password')
	user.send_keys('yourlogin')
	password.send_keys('yourpassword')
	submit = browser.find_element_by_name('submitit')
	submit.submit()
	print('Successful Login')
	time.sleep(2)
	
def wilderness():
  browser.get('https://+yourserver+.outwar.com/world?suid=yourid')
	getToWilderness = browser.find_element_by_css_selector('Wilderness')
	getToWilderness.click()
	while True:
		wilderness = browser.find_element_by_css_selector('#wildernessLink > img:nth-child(1)')
		wilderness.click()
		page = browser.find_element_by_css_selector('#combat_log_link')
		browser.execute_script("window.history.go(-1)")
		time.sleep(1)
		browser.refresh()

browser = init_driver()
login()
wilderness()
