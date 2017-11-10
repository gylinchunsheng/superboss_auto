#coding=utf-8
import time
import unittest

from framework.browser_engine1 import BrowserEngine1
from pageobjects.superboss_homepage import SuperHomePage
from framework.base_page import BasePage

from  selenium import webdriver


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

    def test_orderupdate(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_trade_module() #点击打单模块
        time.sleep(2)
        homepage.click_trade()  #点击打单发货
        time.sleep(3)
        homepage.nowwindow()  #当前窗口
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        homepage.click_update_data()  #点击更新数据
        time.sleep(2)
        driver = self.driver  #初始化
        update_data_framedata = driver.find_element_by_xpath("//*[@id='progress']/div/div/div[1]").text   # 更新数据进度框标题
        print update_data_framedata
        try:
            assert '订单更新' in update_data_framedata
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_singleprint(self):

        homepage = SuperHomePage(self.driver)
        homepage.nowwindow()  # 当前窗口
        time.sleep(2)
        homepage.click_kuaididan_noprint()  #点击未打印tab
        time.sleep(2)
        homepage.click_single_print()  #点击预览/打印
        time.sleep(5)
        homepage.click_single_preview()  # 点击预览/打印
        time.sleep(5)
        homepage.nowwindow()  # 当前窗口
        time.sleep(2)
        try:
            assert 'pdf' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

        #homepage.click_single_send()  # 点击发货
        #time.sleep(2)


    '''
        try:
            assert '发货管理-订单列表' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

'''
if __name__ == '__main__':
    unittest.main()
    # unittest.main(verbosity=2)
