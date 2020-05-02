from selenium import webdriver
from time import sleep
import unittest

class Login_Search(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r'D:\chromedriver\chromedriver.exe')
    def visiturl(self,url):
        # url = eval(url)
        self.driver.get(url[0])
    def find_ele(self,arg):
        self.driver.find_element_by_id(arg[0]).send_keys(arg[1])
    def click_login(self,id):
        self.driver.find_element_by_id(id[0]).click()
        sleep(3)
    def assert_words(self,keywords):
        self.assertIn(keywords[0],self.driver.page_source,'Not found data!')
    def clear_words(self,id):
        self.driver.find_element_by_id(id[0]).clear()

    def test_run(self):
        with open(r'D:\software\pycharm_data\practice\Test_data\KDT_searin_in_baidu.txt',encoding='utf-8') as f:
            for line in f:
                action,data1 = line.split('||')
                exec('self.'+action+'('+data1+')')
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()
