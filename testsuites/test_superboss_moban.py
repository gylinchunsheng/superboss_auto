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


    def test_moban_xqhb(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_moban_module()  # 点击模板模块
        time.sleep(2)
        homepage.click_moban_xqhb()  # 详情海报

        homepage.nowwindow()  # 当前窗口
        time.sleep(2)

        homepage.get_windows_img()  # 调用基类截图方法
        xq_text_link = "xpath=>.//*[@id='detailHaibao']/span"
        el = homepage.get_text(xq_text_link)
        try:
            assert '创建海报' in homepage.get_page_title() and '750详情海报' in el  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_moban_qphb(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_moban_module()  # 点击模板模块
        time.sleep(2)
        homepage.click_moban_qphb()  # 点击全屏海报
        homepage.nowwindow()  # 当前窗口
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        qp_text_link = "xpath=>.//*[@id='screenHaibao']/span"
        el = homepage.get_text(qp_text_link)
        try:
            assert '创建海报' in homepage.get_page_title()  and  '1920全屏海报' in el # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_moban_lbhb(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_moban_module()  # 点击模板模块
        time.sleep(2)
        homepage.click_moban_lbhb()  # 点击轮播海报
        homepage.nowwindow()  # 当前窗口
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        lb_text_link = "xpath=>.//*[@id='groupHaibao']/span"
        el = homepage.get_text(lb_text_link)
        try:
            assert '创建海报' in homepage.get_page_title()  and '1920轮播海报' in el # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_moban_hdhb(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_moban_module()  # 点击模板模块
        time.sleep(2)
        homepage.click_moban_hdhb()  # 点击活动海报
        homepage.nowwindow()  # 当前窗口
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        hd_text_link = "xpath=>.//*[@id='detailHaibao']/span"
        el = homepage.get_text(hd_text_link)
        try:
            assert '创建海报' in homepage.get_page_title()  and '750详情海报' in el # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_moban_bbtj(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_moban_module()  # 点击模板模块
        time.sleep(2)
        homepage.click_moban_bbtj()  # 点击宝贝推荐
        homepage.nowwindow()  # 当前窗口
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        bb_text_link = "xpath=>.//*[@id='container']/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/table/tbody/tr[2]/td[3]/span"
        el = homepage.get_text(bb_text_link)
        try:
            assert '宝贝推荐' in homepage.get_page_title() and '查询' in el # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_moban_ztsy(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_moban_module()  # 点击模板模块
        time.sleep(2)
        homepage.click_moban_ztsy()  # 点击主图水印
        homepage.nowwindow()  # 当前窗口
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        zt_text_link = "xpath=>.//*[@id='container']/div/div[1]/div/div/div[1]/ul/li[1]/span"
        el = homepage.get_text(zt_text_link)
        try:
            assert '折扣水印' in homepage.get_page_title()  and '折扣水印' in el # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_moban_ztsp(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_moban_module()  # 点击模板模块
        time.sleep(2)
        homepage.click_moban_ztsp()  # 点击主图视频
        homepage.nowwindow()  # 当前窗口
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        sp_text_link = "xpath=>.//*[@id='J-ui-step']/div[2]/div/div[1]/div[1]/div/span[3]/form/span"
        el = homepage.get_text(sp_text_link)
        try:
            assert '主图视频' in homepage.get_page_title()  and  '搜索宝贝' in el # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_moban_dptc(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_moban_module()  # 点击模板模块
        time.sleep(2)
        homepage.click_moban_dptc() # 点击搭配套餐
        homepage.nowwindow()  # 当前窗口
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        tc_text_link = "xpath=>.//*[@id='container']/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/table/tbody/tr[2]/td[3]/span"
        el = homepage.get_text(tc_text_link)
        try:
            assert '搭配套餐' in homepage.get_page_title() and  '查询' in el # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_moban_tgtj(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_moban_module()  # 点击模板模块
        time.sleep(2)
        homepage.click_moban_tgtj() # 点击团购推荐
        homepage.nowwindow()  # 当前窗口
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        tg_text_link = "xpath=>.//*[@id='container']/div/div[1]/div/div[2]/div[1]/ul/li[1]/span"
        el = homepage.get_text(tg_text_link)
        try:
            assert '团购推荐' in homepage.get_page_title() and  '全部模板' in el# 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_moban_pjtj(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_moban_module()  # 点击模板模块
        time.sleep(2)
        homepage.click_moban_pjtj()  # 点击评价推荐
        homepage.nowwindow()  # 当前窗口
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        pj_text_link = "xpath=>.//*[@id='container']/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/table/tbody/tr[2]/td[3]/span"
        el = homepage.get_text(pj_text_link)
        try:
            assert '评价推荐' in homepage.get_page_title() and  '查询' in el  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_moban_flmb(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_moban_module()  # 点击模板模块
        time.sleep(2)
        homepage.click_moban_flmb()  # 点击分类模板
        homepage.nowwindow()  # 当前窗口
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        fl_text_link = "xpath=>.//*[@id='templ-box-2510']/div[2]/div[2]/div/a"
        el = homepage.get_text(fl_text_link)
        try:
            assert '分类模板' in homepage.get_page_title() and  '开始制作' in el  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_moban_kfmb(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_moban_module()  # 点击模板模块
        time.sleep(2)
        homepage.click_moban_kfmb()  # 点击客服模板
        homepage.nowwindow()  # 当前窗口
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        kf_text_link = "xpath=>.//*[@id='templ-box-2512']/div[2]/div[2]/div/a"
        el = homepage.get_text(kf_text_link)
        try:
            assert '客服模板' in homepage.get_page_title()  and  '开始制作' in el # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_moban_ccmb(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_moban_module()  # 点击模板模块
        time.sleep(2)
        homepage.click_moban_ccmb()  # 点击尺寸模板
        homepage.nowwindow()  # 当前窗口
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        cc_text_link = "xpath=>.//*[@id='J_slt-industry-btns']/span[1]"
        el = homepage.get_text(cc_text_link)
        try:
            assert '尺寸模板' in homepage.get_page_title() and  '全部' in el  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_moban_mfkt(self):
        homepage = SuperHomePage(self.driver)
        homepage.click_home()  # 调用页面对象类中的点击搜索按钮方法,点击首页
        time.sleep(2)
        homepage.click_moban_module()  # 点击模板模块
        time.sleep(2)
        homepage.click_moban_mfkt()  # 点击魔法抠图
        homepage.nowwindow()  # 当前窗口
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        kt_text_link = "xpath=>.//*[@id='cutMain-search']"
        el = homepage.get_text(kt_text_link)
        try:
            assert '魔法抠图' in homepage.get_page_title() and  '搜索宝贝' in el   # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))
if __name__ == '__main__':
    unittest.main()
    # unittest.main(verbosity=2)
