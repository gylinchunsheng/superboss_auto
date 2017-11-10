# coding=utf-8
import time
from selenium import webdriver
import time
import unittest

#import urllib2
#import re
#from bs4 import BeautifulSoup
#from distutils.filelist import findall



from framework.browser_engine1 import BrowserEngine1
from pageobjects.superboss_homepage import SuperHomePage

class Superboss(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine1(cls)
        cls.driver = browse.open_browser1(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()

    def test_test1(self):

        # homepage = SuperHomePage(self.driver)
        # homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        # time.sleep(2)
        # for link in self.driver.find_elements_by_xpath("//*[@id]"):
        #   print (link.get_attribute('id'))

        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_cuxiao_module()  # 点击促销模块
        time.sleep(2)
        homepage.click_cuxiao_zk()  # 点击折扣
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        zk_text_link = "xpath=>.//*[@id='myNextStep']"  # 折扣

        el = homepage.get_text(zk_text_link)

        try:
            assert '限时折扣' in homepage.get_page_title() and  '下一步：选择宝贝' in el    # 调用页面对象继承基类中的获取页面标题方法
            #assert '下一步：选择宝贝' in el
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

'''
    page = urllib2.urlopen('http://movie.douban.com/top250?format=text')
    contents = page.read()
    # print(contents)
    soup = BeautifulSoup(contents, "html.parser")
    print("豆瓣电影TOP250" + "\n" + " 影片名              评分       评价人数     链接 ")
    for tag in soup.find_all('div', class_='info'):
        # print tag
        m_name = tag.find('span', class_='title').get_text()
        m_rating_score = float(tag.find('span', class_='rating_num').get_text())
        m_people = tag.find('div', class_="star")
        m_span = m_people.findAll('span')
        m_peoplecount = m_span[3].contents[0]
        m_url = tag.find('a').get('href')
        print(m_name + "        " + str(m_rating_score) + "           " + m_peoplecount + "    " + m_url)

'''



