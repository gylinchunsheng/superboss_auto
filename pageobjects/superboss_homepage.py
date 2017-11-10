# -*- coding:utf-8 -*-
from framework.base_page import BasePage


class SuperHomePage(BasePage):
    update_link = "xpath=>.//*[@id='header-nav']/div/div/div/div/div[1]/div[1]/a"  # 首页
    home_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[1]/dl/dt/a"  # 续费升级
    #促销模块
    cuxiao_module_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[2]/dl/dt/a"  # 促销
    cuxiao_zk_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[2]/dl/dd/div[1]/a[1]"  #折扣
    cuxiao_msby_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[2]/dl/dd/div[1]/a[2]"  # 满送包邮
    cuxiao_xsxg_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[2]/dl/dd/div[1]/a[3]"  # 限时限购
    cuxiao_cxgj_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[2]/dl/dd/div[2]/div[1]/a"  # 促销工具
    cuxiao_dpyhq_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[2]/dl/dd/div[2]/div[2]/a"  # 店铺优惠券
    cuxiao_bgyx_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[2]/dl/dd/div[2]/div[3]/a"  # 包裹营销
    cuxiao_hdyx_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[2]/dl/dd/div[2]/div[4]/a"  # 互动营销
    cuxiao_wxyx_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[2]/dl/dd/div[2]/div[5]/a"  # 无线营销
    cuxiao_zwtg_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[2]/dl/dd/div[2]/div[6]/a"  # 站外推广


    def click_cuxiao_module(self):
        self.click(self.cuxiao_module_link)
        self.sleep(2)

    def click_cuxiao_zk(self):
        self.click(self.cuxiao_zk_link)
        self.sleep(2)

    def click_cuxiao_msby(self):
        self.click(self.cuxiao_msby_link)
        self.sleep(2)

    def click_cuxiao_xsxg(self):
        self.click(self.cuxiao_xsxg_link)
        self.sleep(2)

    def click_cuxiao_cxgj(self):
        self.click(self.cuxiao_cxgj_link)
        self.sleep(2)

    def click_cuxiao_dpyhq(self):
        self.click(self.cuxiao_dpyhq_link)
        self.sleep(2)

    def click_cuxiao_bgyx(self):
        self.click(self.cuxiao_bgyx_link)
        self.sleep(2)

    def click_cuxiao_hdyx(self):
        self.click(self.cuxiao_hdyx_link)
        self.sleep(2)

    def click_cuxiao_wxyx(self):
        self.click(self.cuxiao_wxyx_link)
        self.sleep(2)

    def click_cuxiao_zwtg(self):
        self.click(self.cuxiao_zwtg_link)
        self.sleep(2)

    #模板模块
    moban_module_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[3]/dl/dt/a"  # 模板
    moban_xqhb_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[3]/dl/dd/div[1]/a[1]" #详情海报
    moban_qphb_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[3]/dl/dd/div[1]/a[2]"  # 全屏海报
    moban_lbhb_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[3]/dl/dd/div[1]/a[3]"  # 轮播海报

    moban_hdhb_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[3]/dl/dd/div[2]/div[1]/a"  #活动海报
    moban_bbtj_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[3]/dl/dd/div[2]/div[2]/a"  # 宝贝推荐
    moban_ztsy_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[3]/dl/dd/div[2]/div[3]/a"  # 主图水印
    moban_ztsp_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[3]/dl/dd/div[2]/div[4]/a"  # 主图视频
    moban_dptc_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[3]/dl/dd/div[2]/div[5]/a"  # 搭配套餐
    moban_tgtj_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[3]/dl/dd/div[2]/div[6]/a"  # 团购推荐
    moban_pjtj_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[3]/dl/dd/div[2]/div[7]/a"  # 评价推荐
    moban_flmb_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[3]/dl/dd/div[2]/div[8]/a"  # 分类模板
    moban_kfpj_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[3]/dl/dd/div[2]/div[9]/a"  # 客服模板
    moban_ccmb_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[3]/dl/dd/div[2]/div[10]/a"  # 尺寸模板
    moban_mfkt_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[3]/dl/dd/div[2]/div[11]/a"  # 魔法抠图

    def click_moban_module(self):
        self.click(self.moban_module_link)
        self.sleep(2)

    def click_moban_xqhb(self):
        self.click(self.moban_xqhb_link)
        self.sleep(2)

    def click_moban_qphb(self):
        self.click(self.moban_qphb_link)
        self.sleep(2)

    def click_moban_lbhb(self):
        self.click(self.moban_lbhb_link)
        self.sleep(2)

    def click_moban_hdhb(self):
        self.click(self.moban_hdhb_link)
        self.sleep(2)

    def click_moban_bbtj(self):
        self.click(self.moban_bbtj_link)
        self.sleep(2)

    def click_moban_ztsy(self):
        self.click(self.moban_ztsy_link)
        self.sleep(2)

    def click_moban_ztsp(self):
        self.click(self.moban_ztsp_link)
        self.sleep(2)

    def click_moban_dptc(self):
        self.click(self.moban_dptc_link)
        self.sleep(2)

    def click_moban_tgtj(self):
        self.click(self.moban_tgtj_link)
        self.sleep(2)

    def click_moban_pjtj(self):
        self.click(self.moban_pjtj_link)
        self.sleep(2)

    def click_moban_flmb(self):
        self.click(self.moban_flmb_link)
        self.sleep(2)

    def click_moban_kfmb(self):
        self.click(self.moban_kfpj_link)
        self.sleep(2)

    def click_moban_ccmb(self):
        self.click(self.moban_ccmb_link)
        self.sleep(2)

    def click_moban_mfkt(self):
        self.click(self.moban_mfkt_link)
        self.sleep(2)

    #商品模块
    shangpin_module_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[4]/dl/dt/a"  # 商品
    shangpin_plgj_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[4]/dl/dt/a"  # 批量改价
    shangpin_gkc_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[4]/dl/dt/a"  # 改库存
    shangpin_gbt_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[4]/dl/dt/a"  # 改标题

    shangpin_bbgl_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[4]/dl/dd/div[2]/div[1]/a"  # 宝贝管理
    shangpin_bbtb_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[4]/dl/dd/div[2]/div[2]/a"  # 宝贝同步
    shangpin_cctj_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[4]/dl/dd/div[2]/div[3]/a"  # 橱窗推荐
    shangpin_sjxq_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[4]/dl/dd/div[2]/div[4]/a"  # 手机详情
    shangpin_zdsxj_jlink = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[4]/dl/dd/div[2]/div[5]/a"  # 自动上下架
    shangpin_plxg_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[4]/dl/dd/div[2]/div[6]/a"  # 批量修改
    shangpin_wjcjc_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[4]/dl/dd/div[2]/div[7]/a"  # 违禁词检测
    shangpin_bbfz_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[4]/dl/dd/div[2]/div[8]/a"  # 宝贝复制
    shangpin_bbbf_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[4]/dl/dd/div[2]/div[9]/a"  # 宝贝备份
    shangpin_btyh_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[4]/dl/dd/div[2]/div[10]/a"  # 标题优化
    shangpin_cksj_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[4]/dl/dd/div[2]/div[11]/a"  # 仓库上架
    shangpin_ztczs_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[4]/dl/dd/div[2]/div[12]/a"  # 直通车助手

    def click_shangpin_module(self):
        self.click(self.shangpin_module_link)
        self.sleep(2)

    def click_shangpin_plgj(self):
        self.click(self.shangpin_plgj_link)
        self.sleep(2)

    def click_shangpin_gkc(self):
        self.click(self.shangpin_gkc_link)
        self.sleep(2)

    def click_shangpin_gbt(self):
        self.click(self.shangpin_gbt_link)
        self.sleep(2)

    def click_shangpin_bbgl(self):
        self.click(self.shangpin_bbgl_link)
        self.sleep(2)

    def click_shangpin_bbtb(self):
            self.click(self.shangpin_bbtb_link)
            self.sleep(2)

    def click_shangpin_cctj(self):
        self.click(self.shangpin_cctj_link)
        self.sleep(2)

    def click_shangpin_sjxq(self):
        self.click(self.shangpin_sjxq_link)
        self.sleep(2)

    def click_shangpin_zdsxj(self):
        self.click(self.shangpin_zdsxj_jlink)
        self.sleep(2)

    def click_shangpin_plxg(self):
        self.click(self.shangpin_plxg_link)
        self.sleep(2)

    def click_shangpin_wjcjc(self):
        self.click(self.shangpin_wjcjc_link)
        self.sleep(2)

    def click_shangpin_bbfz(self):
        self.click(self.shangpin_bbfz_link)
        self.sleep(2)

    def click_shangpin_bbbf(self):
        self.click(self.shangpin_bbbf_link)
        self.sleep(2)

    def click_shangpin_btyh(self):
        self.click(self.shangpin_btyh_link)
        self.sleep(2)

    def click_shangpin_cksj(self):
        self.click(self.shangpin_cksj_link)
        self.sleep(2)

    def click_shangpin_ztczs(self):
        self.click(self.shangpin_ztczs_link)
        self.sleep(2)

    # 交易模块
    jioayi_module_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[5]/dl/dt/a"  # 交易
    jiaoyi_plpj_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[6]/dl/dt/a"  # 批量评价
    jiaoyi_qdjg_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[6]/dl/dt/a"  # 全店禁购
    jiaoyi_zdpj_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[6]/dl/dt/a"  # 自动评价

    jiaoyi_jygl_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[5]/dl/dd/div[2]/div[1]/a"  # 交易管理
    jiaoyi_pjgl_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[5]/dl/dd/div[2]/div[2]/a"  # 评价管理
    jiaoyi_cps_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[5]/dl/dd/div[2]/div[3]/a"  # 差评师拦截

    def click_jiaoyi_module(self):
        self.click(self.jioayi_module_link)
        self.sleep(2)

    def click_jiaoyi_plpj(self):
        self.click(self.jiaoyi_plpj_link)
        self.sleep(2)

    def click_jiaoyi_qdjg(self):
        self.click(self.jiaoyi_qdjg_link)
        self.sleep(2)

    def click_jiaoyi_zdpj(self):
        self.click(self.jiaoyi_zdpj_link)
        self.sleep(2)

    def click_jiaoyi_jygl(self):
        self.click(self.jiaoyi_jygl_link)
        self.sleep(2)

    def click_jiaoyi_pjgl(self):
        self.click(self.jiaoyi_pjgl_link)
        self.sleep(2)

    def click_jiaoyi_cps(self):
        self.click(self.jiaoyi_cps_link)
        self.sleep(2)

    #打单模块
    trade_module_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[6]/dl/dt/a"  # 打单
    trade_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[6]/dl/dd/div/div[1]/a"  # 打单发货
    trade_elec_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[6]/dl/dd/div/div[2]/a"  # 电子面单
    trade_template_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[6]/dl/dd/div/div[3]/a"  # 模板设计
    trade_aotu_fahuo_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[6]/dl/dd/div/div[4]/a"  # 自动发货
    trade_tool_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[6]/dl/dd/div/div[5]/a"  # 实用工具
    trade_custom_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[6]/dl/dd/div/div[6]/a"  # 自定义打单


    update_data_link = "xpath=>.//*[@id='module_trade_list']/div[1]/div/div/div/span[2]"  # 更新数据

    kuaididannoprint_link = "xpath=>.//*[@id='module_trade_list']/div[4]/div[1]/div[1]/ul/li[1]/a"  # 快递单未打印
    single_print_link = "xpath=>.//*[@id='module_trade_list']/div[4]/div[2]/div[1]/div[2]/div/div[1]/div[10]/span[1]"  # 预览/打印
    single_send_link = "xpath=>.//*[@id='module_trade_list']/div[4]/div[2]/div[1]/div[2]/div/div[1]/div[10]/span[2]"  # 发货
    single_preview_link = "xpath=>html/body/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/div/div/div[2]/div/div[1]/div[4]/span[1]"  # 弹框中预览

    def click_trade_module(self):
        self.click(self.trade_module_link)
        self.sleep(2)

    def click_trade(self):
        self.click(self.trade_link)
        self.sleep(2)

    def click_trade_elec(self):
        self.click(self.trade_elec_link)
        self.sleep(2)

    def click_trade_template(self):
        self.click(self.trade_template_link)
        self.sleep(2)

    def click_trade_auto_fahuo(self):
        self.click(self.trade_aotu_fahuo_link)
        self.sleep(2)

    def click_trade_tool(self):
        self.click(self.trade_tool_link)
        self.sleep(2)

    def click_trade_custom(self):
        self.click(self.trade_custom_link)
        self.sleep(2)


    # 短信模块
    sms_module_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[7]/dl/dt/a"  # 短信
    sms_hyfx_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[7]/dl/dd/div[1]/a[1]"  # 会员分析
    sms_jrgh_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[7]/dl/dd/div[1]/a[2]"  # 节日关怀
    sms_hdcf_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[7]/dl/dd/div[1]/a[3]"  # 活动催付

    sms_hyyx_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[7]/dl/dd/div[2]/div[1]/a"  # 会员营销
    sms_fhtx_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[7]/dl/dd/div[2]/div[2]/a"  # 发货提醒
    sms_dxqf_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[7]/dl/dd/div[2]/div[3]/a"  # 短信群发
    sms_cfk_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[7]/dl/dd/div[2]/div[4]/a"  # 催付款
    sms_hygl_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[7]/dl/dd/div[2]/div[5]/a"  # 会员管理
    sms_hyqy_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[7]/dl/dd/div[2]/div[6]/a"  # 会员权益


    def click_sms_module(self):
        self.click(self.sms_module_link)
        self.sleep(2)

    def click_sms_hyfx(self):
        self.click(self.sms_hyfx_link)
        self.sleep(2)

    def click_sms_jrgh(self):
        self.click(self.sms_jrgh_link)
        self.sleep(2)
    def click_sms_hdcf(self):
        self.click(self.sms_hdcf_link)
        self.sleep(2)

    def click_sms_hyyx(self):
        self.click(self.sms_hyyx_link)
        self.sleep(2)

    def click_sms_fhtx(self):
        self.click(self.sms_fhtx_link)
        self.sleep(2)

    def click_sms_dxqf(self):
        self.click(self.sms_dxqf_link)
        self.sleep(2)

    def click_sms_cfk(self):
        self.click(self.sms_cfk_link)
        self.sleep(2)

    def click_sms_hygl(self):
        self.click(self.sms_hygl_link)
        self.sleep(2)

    def click_sms_hyqy(self):
        self.click(self.sms_hyqy_link)
        self.sleep(2)
    # 数据模块
    data_module_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[8]/dl/dt/a"  # 数据
    data_report_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[8]/dl/dd/div/div[1]/a"  # 数据日报
    data_llfx_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[8]/dl/dd/div/div[2]/a"  # 流量分析
    data_xsfx_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[8]/dl/dd/div/div[3]/a"  # 销售分析
    data_bbfx_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[8]/dl/dd/div/div[4]/a"  # 宝贝分析
    data_yxfx_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[8]/dl/dd/div/div[5]/a"  # 营销分析
    data_lrfx_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[8]/dl/dd/div/div[6]/a"  # 利润分析
    data_yybg_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[8]/dl/dd/div/div[7]/a"  # 运营报告
    data_dptj_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[8]/dl/dd/div/div[8]/a"  # 店铺体检
    data_hqfx_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[8]/dl/dd/div/div[9]/a"  # 行情分析
    data_kfjx_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[8]/dl/dd/div/div[10]/a"  # 客服绩效
    data_sjdp_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[8]/dl/dd/div/div[11]/a"  # 数据大屏

    def click_data_module(self):
        self.click(self.data_module_link)
        self.sleep(2)

    def click_data_report(self):
        self.click(self.data_report_link)
        self.sleep(2)

    def click_data_llfx(self):
        self.click(self.data_llfx_link)
        self.sleep(2)

    def click_data_xsfx(self):
        self.click(self.data_xsfx_link)
        self.sleep(2)

    def click_data_bbfx(self):
        self.click(self.data_bbfx_link)
        self.sleep(2)

    def click_data_yxfx(self):
        self.click(self.data_yxfx_link)
        self.sleep(2)

    def click_data_lrfx(self):
        self.click(self.data_lrfx_link)
        self.sleep(2)

    def click_data_yybg(self):
        self.click(self.data_yybg_link)
        self.sleep(2)

    def click_data_dpty(self):
        self.click(self.data_dptj_link)
        self.sleep(2)

    def click_data_hqfx(self):
        self.click(self.data_hqfx_link)
        self.sleep(2)

    def click_data_kfjx(self):
        self.click(self.data_kfjx_link)
        self.sleep(2)

    def click_data_sjdp(self):
        self.click(self.data_sjdp_link)
        self.sleep(2)
    # 手淘模块
    shoutao_module_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[9]/dl/dt/a"  # 手淘
    shoutao_jxmb_link =  "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[9]/dl/dd/div/div[1]/a"  #精选模板
    shoutao_wdmb_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[9]/dl/dd/div/div[2]/a"  # 我的模板
    shoutao_ttjc_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[9]/dl/dd/div/div[3]/a"  # 天天竞猜
    shoutao_kjjl_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[9]/dl/dd/div/div[4]/a"  # 快捷奖励

    def click_shoutao_module(self):
        self.click(self.shoutao_module_link)
        self.sleep(2)

    def click_shoutao_jxmb(self):
        self.click(self.shoutao_jxmb_link)
        self.sleep(2)

    def click_shoutao_wdmb(self):
        self.click(self.shoutao_wdmb_link)
        self.sleep(2)

    def click_shoutao_ttjc(self):
        self.click(self.shoutao_ttjc_link)
        self.sleep(2)

    def click_shoutao_kjjl(self):
        self.click(self.shoutao_kjjl_link)
        self.sleep(2)

    # 培训模块
    peixun_module_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[10]/dl/dt/a"  # 培训
    peixun_shouye_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[10]/dl/dd/div/div[1]/a"  # 培训首页
    peixun_mfkc_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[10]/dl/dd/div/div[2]/a"  # 免费课程
    peixun_xxpx_link = "xpath=>.//*[@id='header-nav']/div/div/div/ul/li[10]/dl/dd/div/div[3]/a"  # 线下培训

    def click_peixun_module(self):
        self.click(self.peixun_module_link)
        self.sleep(2)

    def click_peixun_shouye(self):
        self.click(self.peixun_shouye_link)
        self.sleep(2)

    def click_peixun_mfkc(self):
        self.click(self.peixun_mfkc_link)
        self.sleep(2)

    def click_peixun_xxpx(self):
        self.click(self.peixun_xxpx_link)
        self.sleep(2)


      #打单发货相关
    def click_update(self):
        self.click(self.update_link)
        self.sleep(2)

    def click_home(self):
        self.click(self.home_link)
        self.sleep(2)

    def click_update_data(self):
        self.click(self.update_data_link)
        self.sleep(2)

    def click_kuaididan_noprint(self):
        self.click(self.kuaididannoprint_link)
        self.sleep(2)

    def click_single_print(self):

        self.click(self.single_print_link)
        self.sleep(2)

    def click_single_send(self):
        self.click(self.single_send_link)
        self.sleep(2)
    def click_single_preview(self):
        self.click(self.single_preview_link)
        self.sleep(2)
