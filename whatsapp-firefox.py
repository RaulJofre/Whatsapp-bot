from selenium import webdriver
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.keys import Keys
import time
import os
import sys

if len(sys.argv)<3:
	print 'Usage: python whatsapp-firefox.py NAME TIMES'
	sys.exit(0)
try:
	times = int(sys.argv[len(sys.argv)-1])
except ValueError:
	print 'Enter No. of Times'
	sys.exit(0)
'''Create a New firefox profile and store web.whatsapp.com initial data by log-in in that profile and add its path in firefoxprofile.'''
'''for help in setting firefox profile view  "http://askubuntu.com/questions/239543/get-the-default-firefox-profile-directory-from-bash" &  "http://stackoverflow.com/questions/20289598/python-selenium-import-my-regular-firefox-profile-add-ons".'''

profile = FirefoxProfile('/home/akul08/.mozilla/firefox/xp3056hf.Whatsapp')
driver = webdriver.Firefox(profile)
driver.maximize_window()
print 'Opening Browser!!'
''' Using Firefox Browser and Opening web.whatsapp.com '''
driver.get('https://web.whatsapp.com')

run = 0
print 'Lets Have Some Fun! ;-)'
while 1:		
		run += 1
		# Find the Input Field.
		inputfield = driver.find_elements_by_class_name('input')
		if not inputfield:
			while  not inputfield:
				print 'Page not loaded waiting for 3 sec.'
				time.sleep(3)
				inputfield = driver.find_elements_by_class_name('input')
		for i in sys.argv[1:-2]:
			inputfield[0].send_keys(i+' ')
		inputfield[0].send_keys(sys.argv[-2])
		while 1:
			side_panel = driver.find_element_by_id('side')
			contact = side_panel.find_elements_by_class_name("chat-title") # Search contact in side panel
			if len(contact)>1:
				for i, x in enumerate(contact): # If multiple contacts are found ,let user choose which one.
					print i, ' ', x.text
				no = input('Enter Contact\'s serial no. Number:\n')
			else:
				no = 0	
			try:
				time.sleep(1) #Wait 1 sec.
				contact[no].click()
				break
			except IndexError: # If the Contact is not Present in this list then exit. 
				print 'No Contact Found, Exiting Program!!!'
				sys.exit(0)
		# Wait for 6 sec to load the contact messages.
		time.sleep(6)
		# Send the message by using send keys.
		inputfield = driver.find_elements_by_class_name('input')
		inputfield[1].send_keys('Brace Yourself Spam Coming!!')
		inputfield[1].send_keys(Keys.RETURN)
		# Or send the same mssg multiple times.
		for i in range(times):
			inputfield[1].send_keys('hi '+str(i) )
			inputfield[1].send_keys(Keys.RETURN)
			# Wait for previous Message to get Tick. And Then Continue
			if not i%10:
				time.sleep(5)
			print i
		print 'Done! Thanx For Using This'
		break