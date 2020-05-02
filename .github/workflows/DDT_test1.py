#coding:utf-8
from selenium import webdriver
from time import sleep
import unittest

class Search_in_baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r'D:\chromedriver\chromedriver.exe')
    def test_search(self):
        with open(r'D:\software\pycharm_data\practice\Test_data\DDT_search_in_baidu.txt',encoding='utf-8') as f:
            for line in f:
                keywords = line.split('||')
                for key in keywords:
                    self.driver.get('https://www.baidu.com/')
                    self.driver.find_element_by_id('kw').send_keys(key.strip())
                    self.driver.find_element_by_id('su').click()
                    sleep(3)
                    self.assertIn(r'百度一下',self.driver.page_source,'Not found data!')
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


