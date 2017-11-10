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


    def test_sms_hyfx(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_sms_module()  # 点击短信模块
        time.sleep(2)
        homepage.click_sms_hyfx()  # 点击会员分析
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        try:
            assert '会员分析' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_sms_jrgh(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_sms_module()  # 点击短信模块
        time.sleep(2)
        homepage.click_sms_jrgh()  # 点击节日关怀
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        try:
            assert '短信群发' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_sms_hdcf(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_sms_module()  # 点击短信模块
        time.sleep(2)
        homepage.click_sms_hdcf()  # 点击活动催付
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        try:
            assert '活动催付' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_sms_hyyx(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_sms_module()  # 点击短信模块
        time.sleep(2)
        homepage.click_sms_hyyx()  # 点击会员营销
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        try:
            assert '会员数据分析' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_sms_fhtx(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_sms_module()  # 点击短信模块
        time.sleep(2)
        homepage.click_sms_fhtx()  # 点击发货提醒
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        try:
            assert '发货提醒' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_sms_dxqf(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_sms_module()  # 点击短信模块
        time.sleep(2)
        homepage.click_sms_dxqf()  # 点击短信群发
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        try:
            assert '会员筛选发送' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_sms_cfk(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_sms_module()  # 点击短信模块
        time.sleep(2)
        homepage.click_sms_cfk()  # 点击催付款
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        try:
            assert '催付提醒' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_sms_hygl(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_sms_module()  # 点击短信模块
        time.sleep(2)
        homepage.click_sms_hygl()  # 点击会员管理
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        try:
            assert '会员分组' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_sms_hyqy(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_sms_module()  # 点击短信模块
        time.sleep(2)
        homepage.click_sms_hyqy()  # 点击会员权益
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        try:
            assert '会员权益' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))


if __name__ == '__main__':
    unittest.main()
    # unittest.main(verbosity=2)
