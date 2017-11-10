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


    def test_cuxiao_zk(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_cuxiao_module()  # 点击促销模块
        time.sleep(2)
        homepage.click_cuxiao_zk()  # 点击折扣
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        zk_text_link = "xpath=>.//*[@id='myNextStep']"  # 折扣
        el = homepage.get_text(zk_text_link)

        try:
            assert '限时折扣' in homepage.get_page_title() and  '下一步：选择宝贝' in el  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_cuxiao_msby(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_cuxiao_module()  # 点击促销模块
        time.sleep(2)
        homepage.click_cuxiao_msby()  # 点击满送包邮
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        ms_text_link = "xpath=>.//*[@id='myNextStep']"  # 折扣
        el = homepage.get_text(ms_text_link)
        try:
            assert '满送' in homepage.get_page_title() and  '下一步：选择宝贝' in el  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_cuxiao_xsxg(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_cuxiao_module()  # 点击促销模块
        time.sleep(2)
        homepage.click_cuxiao_xsxg()  # 点击限时限购
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        xg_text_link = "xpath=>.//*[@id='myNextStep']"  # 折扣
        el = homepage.get_text(xg_text_link)
        try:
            assert '限购' in homepage.get_page_title() and  '下一步：选择宝贝' in el  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_cuxiao_cxgj(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_cuxiao_module()  # 点击促销模块
        time.sleep(2)
        homepage.click_cuxiao_cxgj()  # 点击促销工具
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        cx_text_link = "xpath=>.//*[@id='notend-tab']/span"
        el = homepage.get_text(cx_text_link)
        try:
            assert '活动工具' in homepage.get_page_title() and  '未结束活动' in el # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_cuxiao_dpyhq(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_cuxiao_module()  # 点击促销模块
        time.sleep(2)
        homepage.click_cuxiao_dpyhq()  # 点击店铺优惠券
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        yhq_text_link = "xpath=>.//*[@id='J_app-pages']/div/div[1]/div/div[1]/div[3]/a"
        el = homepage.get_text(yhq_text_link)
        try:
            assert '优惠券' in homepage.get_page_title() and '优惠券列表' in el   # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_cuxiao_bgyx(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_cuxiao_module()  # 点击促销模块
        time.sleep(2)
        homepage.click_cuxiao_bgyx()  # 点击包裹营销
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        bg_text_link = "xpath=>.//*[@id='main-nav']/a[1]"
        el = homepage.get_text(bg_text_link)
        try:
            assert '超级卡片' in homepage.get_page_title() and '首页' in el # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_cuxiao_hdyx(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_cuxiao_module()  # 点击促销模块
        time.sleep(2)
        homepage.click_cuxiao_hdyx()  # 点击互动营销
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        hd_text_link = "xpath=>.//*[@id='active-list-nav']/li[1]/span"
        el = homepage.get_text(hd_text_link)
        try:
            assert '互动营销' in homepage.get_page_title() and '正在进行中' in el  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_cuxiao_wxyx(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_cuxiao_module()  # 点击促销模块
        time.sleep(2)
        homepage.click_cuxiao_wxyx() # 点击无线营销
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        wx_text_link = "xpath=>.//*[@id='activityList']/div[2]/div[1]/div/div/div/div/div[2]/div"
        el = homepage.get_text(wx_text_link)
        try:
            assert '活动列表' in homepage.get_page_title() and '进行中' in el # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_cuxiao_azwtg(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_cuxiao_module()  # 点击促销模块
        time.sleep(2)
        homepage.click_cuxiao_zwtg() # 点击站外推广
        homepage.nowwindow()  # 当前窗口
        time.sleep(4)
        homepage.get_windows_img()  # 调用基类截图方法
        homepage.close_popup()  # 点击弹出上面的确认按钮
        time.sleep(2)
        zw_text_link = "xpath=>.//*[@id='container']/div/div[1]/div/div[1]/div[1]/div"
        el = homepage.get_text(zw_text_link)

        try:
            assert '账号管理' in homepage.get_page_title() and '绑定' in el # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))


if __name__ == '__main__':
    unittest.main()
    # unittest.main(verbosity=2)
