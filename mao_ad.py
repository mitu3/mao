from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time



class ad_test():


    def __init__(self):
        self.chromedriver = 'C:\\Users\\bxm\AppData\Local\Programs\Python\Python36\chromedriver.exe'
        self.chome_options = webdriver.ChromeOptions()
        # self.chome_options.add_argument('--proxy-server=http://110.73.52.55:8123')
        mobileEmulation = {'deviceName': 'Galaxy S5'}
        self.chome_options.add_experimental_option('mobileEmulation', mobileEmulation)
        os.environ["webdriver.chrome.driver"] = self.chromedriver
        self.driver = webdriver.Chrome(self.chromedriver, chrome_options=self.chome_options)
        self.url = 'http://m.cudaojia.com/distt/eggModel/show/egg12506.html?business=money-1&' \
                   'appkey=32bb6e97ac7e44328643fccab4f47287&uid=DFDD450A089821023BB7AF1C35DB31&' \
                   'activityid=12506&i=__IMEI__&f=__IDFA__&gettime=1518078204570#page2'
        # self.url = 'http://47.96.253.233:18501/common/findAll?typegroupid=ae'
        # self.url = 'http://httpbin.org/ip'
        self.locator = (By.XPATH, '//*[@id="egg"]/div[6]/div[2]/div[1]/button[1]')
        self.locator2 = (By.XPATH, '//*[@id="dialog5"]/div[3]/div[3]/div[2]')


    def test(self):
        self.driver.get(self.url)
        print("test")
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(self.locator))



    def find_element(self):


        self.dans = '//*[@id="egg"]/div[6]/div[2]/div[1]/button[1]'
        self.jiang = '//*[@id="dialog5"]/div[3]/div[3]/div[2]'



    def throughput(self):
        for i in range(1,9):

            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="egg"]/div[6]/div[2]/div[{}]/button[1]'.format(i)).click()
            print(WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(self.locator2)))
            time.sleep(3)
            self.driver.find_element_by_xpath(self.jiang).click()
            time.sleep(2)
            self.driver.back()




t=ad_test()
t.test()
t.find_element()
t.throughput()