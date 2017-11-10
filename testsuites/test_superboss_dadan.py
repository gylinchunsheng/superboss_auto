#coding=utf-8
import time
import unittest

from framework.browser_engine1 import BrowserEngine1
from pageobjects.superboss_homepage import SuperHomePage


# from  selenium import webdriver


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


    def test_trade(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_trade_module()  # 点击打单模块
        time.sleep(2)
        homepage.click_trade()  # 点击打单发货
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        try:
            assert '发货管理-订单列表' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_trade_elec(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_trade_module()  # 点击打单模块
        time.sleep(2)
        homepage.click_trade_elec()  # 点击电子面单
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        try:
            assert '发货管理' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_trade_template(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_trade_module()  # 点击打单模块
        time.sleep(2)
        homepage.click_trade_template()  # 点击模板设计
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        try:
            assert '云打印面单列表' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_trade_cxgj(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_trade_module()  # 点击打单模块
        time.sleep(2)
        homepage.click_trade_auto_fahuo()  # 点击自动发货
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        try:
            assert '自动发货' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_trade_dpyhq(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_trade_module()  # 点击打单模块
        time.sleep(2)
        homepage.click_trade_tool()  # 点击实用工具
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        try:
            assert '消息中心' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_trade_bgyx(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_trade_module()  # 点击打单模块
        time.sleep(2)
        homepage.click_trade_custom()  # 点击自定义打单
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        try:
            assert '发货管理' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))



if __name__ == '__main__':
    unittest.main()
    # unittest.main(verbosity=2)
