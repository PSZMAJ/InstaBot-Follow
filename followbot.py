# -*- coding: utf-8 -*-
from selenium import webdriver
import time 
import random

class InstaPy():
    
    def __init__(self):
        print(""" 
              
██╗███╗   ██╗███████╗████████╗ █████╗ ██████╗  ██████╗ ████████╗
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝
██║██╔██╗ ██║███████╗   ██║   ███████║██████╔╝██║   ██║   ██║   
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██╔══██╗██║   ██║   ██║   
██║██║ ╚████║███████║   ██║   ██║  ██║██████╔╝╚██████╔╝   ██║   
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═════╝  ╚═════╝    ╚═╝   
                                                                
              
Bot do Follow na Instagramie. Wersja 1.0
Autorem skryptu jest Przemysław Szmaj.
instagram: _h4ker
Za chwile narzędzie rozpocznie prace.
              
              """)
        time.sleep(5)
        self.browser = webdriver.Firefox()  
        
 
        
    ### ---> login
    ###Function is responsible for open browser and login with username and password.
    def login(self):
        self.login = "" ##<--- add your login
        self.password = "" ##<--- add your password
        self.browser.get('https://www.instagram.com/')
        time.sleep(2)
    ##---> click to accept cookies.    
        self.acceptbutton = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]')
        time.sleep(1)
        self.acceptbutton.click()
        time.sleep(1)
    ##---> end     
        self.emailForm = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
        self.emailForm.click()
        self.emailForm.send_keys(self.login)
        time.sleep(2)
        self.passwordForm = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
        self.passwordForm.click()
        self.passwordForm.send_keys(self.password)
        time.sleep(1)
        self.loginButton = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]')
        time.sleep(1)
        self.loginButton.click()
        time.sleep(4)


    ### ---> add_hashtag
    ### Function is responsible for open and run browser with  hashtag form 
    def add_hashtag(self):   
        
        self.hashtags = 'polska' ##<-- add your hashtag
        time.sleep(4)
        self.browser.get('https://www.instagram.com/explore/tags/' + self.hashtags + '/' )
        time.sleep(3)
        self.rand = random.randint(1000,3000)
        self.rand = str(self.rand)
        self.browser.refresh()
        time.sleep(5)
        self.browser.execute_script("window.scrollTo(10," + self.rand + ")")
        print('current #', self.hashtags)
        
    
    ### ---> open_photo
    ### Function is responsible for open random picture on website.     
    def open_photo(self): 
        
        self.left = random.randint(1,3)
        self.left = str(self.left)
        self.downIndex = random.randint(1,3)
        self.downIndex = str(self.downIndex)
        self.photo = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div['+ self.left + ']/div['+ self.downIndex +']/a/div')
        self.photo.click()
        time.sleep(2)
        
        
    ### ---> skip_photo
    ### Function is responsible for random skipp to next photo.    
    def skip_photo(self):
        time.sleep(2)
        self.skip_photo_button = self.browser.find_element_by_link_text('Dalej')
        self.logic_skip_photo = random.randint(1,7)
        self.i = 0
        while self.i < self.logic_skip_photo:
            time.sleep(3)
            self.skip_photo_button = self.browser.find_element_by_link_text('Dalej')
            time.sleep(2)
            self.skip_photo_button.click()
            self.i = self.i + 1
            print('skip {} photo, {}'.format(self.logic_skip_photo, self.i))    
            
     
    ### ---> follow_user_and_get_info
    ### Function is responsible for get user name and click follow
    def follow_user_and_get_info(self):
        time.sleep(2)
        self.follow_button = self.browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')
        time.sleep(2)
        self.get_name = self.browser.find_element_by_class_name('e1e1d')
        time.sleep(0.5)
        self.get_name.text
        print('follow user: {}'.format(self.get_name.text))
        self.follow_button.click()    
        
        
    ### ---> next_photo
    ### Function is responsible for click to next photo.  
    def next_photo(self):
        time.sleep(1)
        self.next_photo_button = self.browser.find_element_by_link_text('Dalej')
        time.sleep(2)
        self.next_photo_button.click()
     
        
    ### ---> relax
    ### Function is responsible for pause.   
    def relax(self):
        self.relax_time = random.randint(305,999)
        print('InstaBot has stopped at this moment. The system will boot up in ', self.relax_time, ' seconds')
        time.sleep(self.relax_time)
        
        
    ### ---> random like
    ### Function is responsible random quantity like.     
    def random_follow(self):
        self.amount = random.randint(49,79) # ammount follow for # sesion.
        print('quantity follow at this session - ', self.amount)
        
        
    ### ---> run
    ### Function is responsible for auto follow user. 
    def run(self):
        
        self.random_follow()
        p_liked = 0
        while True:
            
          if p_liked == self.amount: # liczba przejsc petli:
              p_liked = 0
              self.relax()
              self.browser.refresh()
              time.sleep(2)
              try:
                  self.open_photo()
              except Exception:     
                  self.open_photo()
              time.sleep(2)
              self.skip_photo()
          else:
            time.sleep(5)
            try:
                self.follow_user_and_get_info()
            except Exception:     
                self.next_photo()       
            self.relax_after_follow = random.randint(2,8)
            time.sleep(self.relax_after_follow)
            self.next_photo()
            p_liked = p_liked + 1

bot = InstaPy()
bot.login()
bot.add_hashtag()     
bot.open_photo()   
bot.skip_photo()
bot.run()
