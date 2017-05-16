#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/8 16:43
# @Author  : Nxy
# @Site    : 
# @File    : run_common_help.py
# @Software: PyCharm

import time
from testCase.models import myUnitChrome
from testCase.models.paperDetection.payOption import PayOption
from testCase.models.userVer.userVer import UserVer
from testResult.getResultImage import getResultImage
from util.toolUtils.getPath import GetPath

class RunPay(myUnitChrome.UnitChrome):

    def user_login(self):
        '''用户登录'''
        user_login = UserVer(self.driver)
        user_login.userLogin(username="collegecheck.student2233",password="123456")

    def test_mywallet_pay_1(self):
        self.user_login()
        po = PayOption(self.driver)
        username="collegecheckstudent2233"
        titleInfo="我的钱包支付"
        authorInfo="nxy_1"
        filename = GetPath().getAbsoluteFilePath("200Words.txt","pDeteSingleUpload\\200Words.txt")
        po.user_mywallet_pay(username,titleInfo,authorInfo,filename)
        print("支付完成进入查看 报告页面")
        time.sleep(5)
        altertxt = self.close_alert_and_get_its_text()
        time.sleep(5)
        self.assertEqual("检测结束，是否查看检测结果",altertxt)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"mywallet_pay_ok.jpg")


    def test_union_pay_1(self):
        print("暂不进行测试")

    def test_ali_pay_1(self):
        print("暂不进行测试")

    def test_chongzhi_1(self):
        print("暂不进行测试")

    def test_other_login_1(self):
        self.user_login()
        po = PayOption(self.driver)
        titleInfo="其他用户登录"
        authorInfo="nxy_1"
        filename = GetPath().getAbsoluteFilePath("200Words.txt","pDeteSingleUpload\\200Words.txt")
        po.detection_input(titleInfo,authorInfo,filename)
        time.sleep(5)
        po.other_user_login()
        time.sleep(1)
        divFlag = po.login_div()
        print(divFlag)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"other_user_ok.jpg")


    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        except Exception as e:
            print("alter 弹框出错"%e)