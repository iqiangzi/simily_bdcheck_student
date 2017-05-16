#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/8 17:19
# @Author  : Nxy
# @Site    : 
# @File    : run_paperDetection_detectionInfo.py
# @Software: PyCharm
from testtools.testcase import unittest

from testCase.models import myUnitChrome
import time
from testCase.models.help.help import Help
from testCase.models.paperDetection.detectionInfo import DetectionInfo
from testCase.models.userVer.userVer import UserVer
from testResult.getResultImage import getResultImage


class RunDetection(myUnitChrome.UnitChrome):

    def user_login(self):
        '''用户登录'''
        user_login = UserVer(self.driver)
        user_login.userLogin(username="collegecheck.student2233",password="123456")

    def test_fulltext_look_1(self):
        '''用户在线查看全文报告'''
        self.user_login()
        time.sleep(2)
        detetest = DetectionInfo(self.driver)
        detetest.detection_fulltext_look()
        #获取页面截图
        time.sleep(2)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"childAccount_fulltext_look.jpg")

    def test_detail_download_2(self):
        '''用户详细报告下载'''
        self.user_login()
        time.sleep(2)
        detetest = DetectionInfo(self.driver)
        detetest.detection_detail_download()
        time.sleep(2)
    def test_redetection_3(self):
        '''文本提取错误，用户选择重新检测'''
        self.user_login()
        time.sleep(2)
        detetest = DetectionInfo(self.driver)
        detetest.gotoPageSize("50")
        detetest.gotoPageNum("2")
        time.sleep(2)
        detetest.detection_detail_download()
        time.sleep(1)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"childAccount_redetection.jpg")


if __name__=='__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    s = RunDetection(myUnitChrome.UnitChrome)
    suite.addTest(s.test_fulltext_look_1())
    suite.addTest(s.test_detail_download_2())
    suite.addTest(s.test_redetection_3())
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)