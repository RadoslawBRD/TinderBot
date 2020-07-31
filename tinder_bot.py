#virtualenv <name>
#venv\Script\activate
#python -i tinder_bot.py

from time import sleep
from selenium import webdriver
import random
class TinderBot():
    def __init__(self):
        options = webdriver.ChromeOptions()
            
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(options=options)
    def end(self):
        self.driver.quit()
    def login(self):
        
        self.driver.get('https://tinder.com')
        sleep(6)

        coockie_btn=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        coockie_btn.click()
        #more_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
        #more_btn.click()
        #sleep(1)

        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')

        fb_btn.click()
        
        #base window + switch to login window
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        #login
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        
        email_in.send_keys('<login>')
        pw_in.send_keys('<password>')
        login_btn.click()
        #oczekiwanie aż użytkownik wprowadzi 2FA
        input("Press enter to continue...")            
        self.driver.switch_to_window(self.driver.window_handles[0])
        sleep(1)

        loc_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        loc_btn.click()
        sleep(1)


        noti_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
        noti_btn.click()
        sleep(1)
        try:
            passp_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
            passp_btn.click()
        except:
            print("Usunęli okienko z paszportem od covid")

    def like(self):
        
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()


    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()


    def auto_swipe(self):
        try:
            while True:
                sleep(random.randint(5,10)/10)
                try:
                    if(random.randint(0,100)<72):
                        self.like()
                    else:
                        self.dislike()
                except:
                    try: ##przycisk o dodanie do pulpitu
                        startScreen_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
                        startScreen_btn.click()
                    except:
                        try:
                            noMoreLikes_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]')
                            noMoreLikes_btn.click()
                            print("You're out of likes")
                            break
                        except:
                            print("kolejny blad ;)")
                            #brakuje klikania gdy znajde pare
        except KeyboardInterrupt:
            pass

#bot = TinderBot()
#bot.login()
#bot.like()
#bot.dislike()
#bot.auto_swipe()
