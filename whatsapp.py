from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.keys import Keys
import time
import os
''' Download and place the chrome driver in Downloads folder and 
	edit the following path. '''
chromedriver = "/home/akul08/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

driver.maximize_window()
''' Using Chrome Browser and Opening web.whatsapp.com '''
driver.get('https://web.whatsapp.com')

''' You Need to Scan QR Code Using Your mobile whatsapp EveryTime You run This sript. '''
x = 1
run = 0
print 'Lets Have Some Fun! ;-)'
while x:
	try:
		run += 1
		y = 1
		while y:
			''' Edit the group variable's value and change it to the selected contact or group's "data-reactid". View it from the Developer Tools. '''
			group = driver.find_element_by_xpath(".//*[contains(@data-reactid, '#Enter The contact's data-reactid here#')]")
			try:
				time.sleep(1) #Wait 1 sec.
				group.click()
				y = 0
			except WebDriverException: # If the Contact is not Visible in this list then scroll down. 
				print 'moving down'
		# Find the Input Field.
		inputfield = driver.find_elements_by_class_name('input')
		# Wait for 10 sec to load the contact messages.
		time.sleep(6)
		# Send the message by using send keys.
		inputfield[1].send_keys('hi!')
		inputfield[1].send_keys(Keys.RETURN)
		# Or send the same mssg multiple times.
		for i in range(10):
			inputfield[1].send_keys('Mast Program hai!!')
			inputfield[1].send_keys(Keys.RETURN)
			# Wait for previous Message to get Tick. And Then Continue
			if not i%10:
				time.sleep(3)
		print 'Done! Thanx For Using This'
		x = 0
	except NoSuchElementException: # If the Page is Not Loaded
		if run < 15:
			print 'sleep 5'
			time.sleep(5)
		else:
			print 'Sorry The Contact Not Found!!'
