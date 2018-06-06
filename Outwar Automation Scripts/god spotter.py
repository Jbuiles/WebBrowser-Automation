import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

options = Options()
options.set_headless(headless=True)

login= 'YOURUSERNAME'
password='YOURPASSWORD'
server= 'YOURSERVER'
gods=[]


def init_driver():
    browser = webdriver.Firefox(firefox_options=options, executable_path=r'C:\Users\YOURUSER\AppData\Local\Programs\Python\Python36-32\geckodriver.exe')
    browser.wait = WebDriverWait(browser, 10)
    return browser

def login():
	browser.get('https://'+server+'.outwar.com/login')
	user = browser.find_element_by_name('login_username')
	password = browser.find_element_by_name('login_password')
	user.send_keys(login)
	password.send_keys(password)
	submit = browser.find_element_by_name('submitit')
	submit.submit()
	print('Successful Login')
	time.sleep(2)
	
def godspotter():
	try:
		browser.get('http://'+server+'.outwar.com/raidtools')
		table ='/html/body/center/div/div[3]/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr' #Location of boss info
		rowCount=browser.find_elements_by_xpath(table)
		x=2 #controls row loop. START AT row 2
		y=1 #controls column loop [1-2]
		Tablelen=(len(rowCount))#Count how many bosses are spawned
		while (x <= Tablelen): #Iterate through HTML table. Each iteration of x has 2 y's
			while (y < 3):
				result=browser.wait.until(EC.presence_of_element_located(
					(By.XPATH, '//tr['+str(x)+']/td['+str(y)+']/strong/a/font')))
				name= result.get_attribute('innerHTML')
				name= name.split("Teleport to ")[1]#Strip unecessary words
				gods.append(name)
				y+=1
			y=1#Columns only go up to 2 so this resets it back to 1 for the next iteration of x
			x+=1# Starts the next row iteration
		print(gods)

	except TimeoutException:
		print(gods)
		browser.close()


browser = init_driver()
login()
godspotter()
