from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
import string
import time

"""place your comments to your wish"""
comments = [ 'Nice from fox trading solutions ',  ' hi from fox trading solutions ', 'learn something new from fox trading solutions ', 'Mind blowing from fox trading solutions ',]


posts=0 # No of post it is commenting


browser = webdriver.ChromeOptions() #Chromedriver path.
browser.add_argument("start-maximized");
browser.add_argument("disable-infobars")
browser.add_argument("--disable-extensions")
browser = webdriver.Chrome(chrome_options=browser, executable_path=r'C:\Users\Manan\Desktop\chromedriver.exe') # <----- ENTER PATH HERE
browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher') #website you require to automate

sleep(2)


def Comment():  #Comments the first 9 posts
	global posts
	for y in range (1,4):
		for x in range(1,4):
			post = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/div/div[1]/div[2]')
			browser.implicitly_wait(5)
			post.click()
			sleep(2)
			postcomment = browser.find_element_by_class_name('_9AhH0')  #check out the class as per the browser and the instagram accounts by clicking in inspect element on the page
			sleep(2)
			comment = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').click() #xpath might change account to accounts
			sleep(3)
			comment = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').click() #xpath might change account to accounts
			sleep(3)
			comment = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(random.choice(comments)) #xpath might change account to accounts
			sleep(3)
			sendComment = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button') #xpath might change account to accounts
			sleep(4)
			sendComment.click()
			sleep(4)
			closePost=browser.find_element_by_xpath('/html/body/div[4]/div[3]/button')
			closePost.click()
			browser.refresh()
			sleep(4)
			posts+=1
			sleep(3)
		print ('Nr. of posts: ' +str(posts))

	sleep(5)
	browser.get('https://www.instagram.com/explore/')
	sleep(6)
	Comment()


def start():
	username = browser.find_element_by_name('username')
	username.send_keys('Enter INSTAGRAM USERNAME HERE') 
	password = browser.find_element_by_name('password')
	password.send_keys('ENter INSTAGRAM PASSWORD HERE')
	nextButton = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button')
	nextButton.click()
	sleep(4)
	notification = browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
	notification.click()
	browser.get('https://www.instagram.com/explore/')
	sleep(6)
	Comment()
	sleep(5)


#Start the programm
start()
