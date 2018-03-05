from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time



class ad_test():


    def __init__(self):
        self.chromedriver = 'C:\Users\Administrator\Desktop\chromedriver.exe'
        self.chome_options = webdriver.ChromeOptions()
        # self.chome_options.add_argument('--proxy-server=http://117.28.145.140:35081')
        mobileEmulation = {'deviceName': 'Galaxy S5'}
        self.chome_options.add_experimental_option('mobileEmulation', mobileEmulation)
        os.environ["webdriver.chrome.driver"] = self.chromedriver
        self.chome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(self.chromedriver, chrome_options=self.chome_options)
        self.url = 'http://m.cudaojia.com/distt/eggModel/show/egg12506.html?business=money-1&' \
                   'appkey=32bb6e97ac7e44328643fccab4f47287&uid=DFDD450A089821023BB7A{}&' \
                   'activityid=12506&i=__IMEI__&f=__IDFA__&gettime={}#page2'.format(time.time()*10,time.time())
        # self.url = 'http://47.96.253.233:18501/common/findAll?typegroupid=ae'
        # self.url = 'http://httpbin.org/ip'
        print(self.url)
        self.locator = (By.XPATH, '//*[@id="egg"]/div[6]/div[2]/div[1]/button[1]')
        self.locator2 = (By.XPATH, '//*[@id="dialog5"]/div[3]/div[3]/div[2]')


    def test(self):
        self.driver.get(self.url)
        print("test")
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(self.locator))
        self.now_handle = self.driver.current_window_handle
        return self.driver


    def find_element(self):


        self.dans = '//*[@id="egg"]/div[6]/div[2]/div[9]/button[1]'
        self.jiang = '//*[@id="dialog5"]/div[3]/div[3]/div[2]'



    def throughput(self):
        for i in range(1,9):

            time.sleep(3)
            # WebDriverWait(self.driver, 20, 0.5).until(EC.element_to_be_clickable(self.locator))
            self.driver.find_element_by_xpath('//*[@id="egg"]/div[6]/div[2]/div[{}]/button[1]'.format(i)).click()
            print(i)
            WebDriverWait(self.driver, 20, 0.5).until(EC.element_to_be_clickable(self.locator2))
            # time.sleep(3)
            self.driver.find_element_by_xpath(self.jiang).click()
            time.sleep(0.5)
            self.driver.back()
            self.driver.switch_to.window(self.now_handle)




def run():
    try:
        t=ad_test()
        a = t.test()
        t.find_element()
        t.throughput()
        a.close()
    except Exception:
        print("chongqi")
        a.close()



for i in range(20):
    run()