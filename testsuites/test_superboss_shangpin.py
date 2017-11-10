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


    def test_shangpin_plgj(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_shangpin_module()  # 点击商品模块
        time.sleep(2)
        homepage.click_shangpin_plgj()  # 批量改价

        homepage.nowwindow()  # 当前窗口
        time.sleep(2)

        homepage.get_windows_img()  # 调用基类截图方法

        try:
            assert '批量修改' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_shangpin_gkc(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_shangpin_module()  # 点击商品模块
        time.sleep(2)
        homepage.click_shangpin_gkc()  # 点击改库存
        homepage.nowwindow()  # 当前窗口
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法

        #需要再细化
        try:
            assert '批量修改' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_shangpin_gbt(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_shangpin_module()  # 点击商品模块
        time.sleep(2)
        homepage.click_shangpin_gbt()  # 点击改标题
        homepage.nowwindow()  # 当前窗口
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        try:
            assert '批量修改' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_shangpin_bbtb(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_shangpin_module()  # 点击商品模块
        time.sleep(2)
        homepage.click_shangpin_bbtb()  # 点击宝贝同步
        homepage.nowwindow()  # 当前窗口
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        try:
            assert '宝贝管理' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_shangpin_cctj(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_shangpin_module()  # 点击商品模块
        time.sleep(2)
        homepage.click_shangpin_cctj()  # 点击橱窗推荐
        homepage.nowwindow()  # 当前窗口
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        try:
            assert '橱窗首页' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_shangpin_skxq(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_shangpin_module()  # 点击商品模块
        time.sleep(2)
        homepage.click_shangpin_sjxq()  # 点击手机详情
        homepage.nowwindow()  # 当前窗口
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        try:
            assert '手机详情' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_shangpin_zdsxj(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_shangpin_module()  # 点击商品模块
        time.sleep(2)
        homepage.click_shangpin_zdsxj()  # 点击自动上下架
        homepage.nowwindow()  # 当前窗口
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        try:
            assert '自动上下架' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_shangpin_plxg(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_shangpin_module()  # 点击商品模块
        time.sleep(2)
        homepage.click_shangpin_plxg() # 点击批量修改
        homepage.nowwindow()  # 当前窗口
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        try:
            assert '批量修改' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_shangpin_wjc(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_shangpin_module()  # 点击商品模块
        time.sleep(2)
        homepage.click_shangpin_wjc()   # 点击违禁词检测
        homepage.nowwindow()  # 当前窗口
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        try:
            assert '违禁词扫描' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_shangpin_bbfz(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_shangpin_module()  # 点击商品模块
        time.sleep(2)
        homepage.click_shangpin_bbfz()  # 点击宝贝复制
        homepage.nowwindow()  # 当前窗口
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        try:
            assert '选择宝贝' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_shangpin_bbbf(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_shangpin_module()  # 点击商品模块
        time.sleep(2)
        homepage.click_shangpin_bbbf()  # 点击宝贝备份
        homepage.nowwindow()  # 当前窗口
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        try:
            assert '首页' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_shangpin_btyh(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_shangpin_module()  # 点击商品模块
        time.sleep(2)
        homepage.click_shangpin_btyh()  # 点击标题优化
        homepage.nowwindow()  # 当前窗口
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        try:
            assert '标题诊断' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_shangpin_cksj(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_shangpin_module()  # 点击商品模块
        time.sleep(2)
        homepage.click_shangpin_cksj()  # 点击仓库上架
        homepage.nowwindow()  # 当前窗口
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        try:
            assert '仓库上架' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_shangpin_ztczs(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_shangpin_module()  # 点击商品模块
        time.sleep(2)
        homepage.click_shangpin_ztczs()  # 点击直通车助手
        homepage.nowwindow()  # 当前窗口
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        try:
            assert '直通车助手' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))
if __name__ == '__main__':
    unittest.main()
    # unittest.main(verbosity=2)
