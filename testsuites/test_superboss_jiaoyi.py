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


    def test_jiaoyi_plpj(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_jiaoyi_module()  # 点击交易模块
        time.sleep(2)
        homepage.click_jiaoyi_plpj()  # 批量评价
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        try:
            assert '批量评价' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_jiaoyi_qdjg(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_jiaoyi_module()  # 点击交易模块
        time.sleep(2)
        homepage.click_jiaoyi_qdjg()  # 点击全店禁购
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        try:
            assert '禁购名单' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_jiaoyi_zdpj(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_jiaoyi_module()  # 点击交易模块
        time.sleep(2)
        homepage.click_jiaoyi_zdpj()  # 点击自动评价
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        try:
            assert '自动评价' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_jiaoyi_pjgl(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_jiaoyi_module()  # 点击交易模块
        time.sleep(2)
        homepage.click_jiaoyi_pjgl()  # 点击评价管理
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        try:
            assert '中差评管理' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_jiaoyi_cps(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_jiaoyi_module()  # 点击交易模块
        time.sleep(2)
        homepage.click_jiaoyi_cps()  # 点击差评师拦截
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        try:
            assert '差评师拦截' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))



if __name__ == '__main__':
    unittest.main()
    # unittest.main(verbosity=2)
