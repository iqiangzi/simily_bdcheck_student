#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-28 10:01:50
# @Author  : Nxy
# @Site    : 
# @File    : run_manualEntry.py
# @Software: PyCharm
from selenium import  webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from testCase.models import myUnitChrome
from testCase.models import myUnitFirefox
from testCase.models.paperDetection.manualEntry import ManualEntry
from testCase.models.userVer.userVer import UserVer
from testResult.getResultImage import getResultImage
from util.commonUtils.fileOption import FilesOption
from util.toolUtils.getPath import GetPath


class RunManualEntry(myUnitChrome.UnitChrome):
    def user_login(self):
        '''用户登录'''
        user_login = UserVer(self.driver)
        user_login.userLogin(username="collegecheck.student2233",password="123456")

    def ManualOption(self,titleInfo,authorInfo,textInfo):
        self.user_login()
        time.sleep(2)
        manu = ManualEntry(self.driver)
        manu.manualEntryOption(titleInfo,authorInfo,textInfo)

    def ManualNoText(self,titleInfo,authorInfo):
        self.user_login()
        time.sleep(2)
        manu = ManualEntry(self.driver)
        manu.manualEntry(titleInfo,authorInfo)




    def test_manual_info_null_1(self):
        '''必填信息为空，无法检测'''
        self.ManualOption("","","")
        manu = ManualEntry(self.driver)
        self.assertEqual(manu.title_null_mind(),"请输入题名")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"manual_info_null.jpg")

    def test_manual_title_null_2(self):
        '''标题为空，无法检测'''
        self.ManualOption("","作者","文本")
        manu = ManualEntry(self.driver)
        self.assertEqual(manu.title_null_mind(),"请输入题名")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"manual_title_null.jpg")

    def test_manual_author_null_3(self):
        '''作者为空，无法检测'''
        self.ManualOption("作者为空","","文本")
        manu = ManualEntry(self.driver)
        self.assertEqual(manu.author_null_mind(),"请输入作者")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"manual_author_null.jpg")

    def test_manual_text_null_4(self):
        '''文本为空，无法检测'''
        self.ManualOption("文本为空","作者","")
        manu = ManualEntry(self.driver)
        self.assertEqual(manu.text_null_mind(),"请输入内容")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"manual_text_null.jpg")

    def test_manual_title_long_5(self):
        '''标题超过50个限制长度，无法检测'''
        titleInfo="测试信息标题超过50个限制测试信息标题超过50个限制测试信息标题超过50个限制测试信息标题超过50个限制测试1"
        self.ManualOption(titleInfo,"作者","文本信息")
        time.sleep(1)
        altertext= self.close_alert_and_get_its_text()
        time.sleep(1)
        self.assertEqual(altertext,"题名长度不得大于50")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"manual_title_long.jpg")

    def test_manual_author_long_6(self):
        '''作者超过50个限制长度，无法检测'''
        authorInfo="测试信息作者超过50个限制测试信息作者超过50个限制测试信息作者超过50个限制测试信息作者超过50个限制测试1"
        self.ManualOption("作者信息超过50",authorInfo,"文本信息")
        time.sleep(1)
        altertext= self.close_alert_and_get_its_text()
        time.sleep(1)
        self.assertEqual(altertext,"作者长度不得大于50")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"manual_author_long.jpg")

    def test_manual_text_short_7(self):
        '''文本信息不足200长度，无法检测'''
        textInfo="测试信息作者超过50个限制测试信息作者超过50个限制测试信息作者超过50个限制测试信息作者超过50个限制测试1"
        self.ManualOption("文本信息不足200","作者",textInfo)
        manu = ManualEntry(self.driver)
        time.sleep(1)
        altertext= self.close_alert_and_get_its_text()
        time.sleep(1)
        self.assertEqual(altertext,"字数不得少于200,不得大于100000")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"manual_text_short.jpg")
    def test_manual_text_long_8(self):
        '''文本信息超过100万长度，无法检测'''
        f = FilesOption()
        g = GetPath()
        manu = ManualEntry(self.driver)
        filePath =g.getAbsoluteFilePath("big_text.txt",r"paperDetectionManu\\big_text.txt")
        Flist = f.readFileContent(filePath)
        self.ManualNoText("文本信息超过100万","作者")
        for i in range(0,len(Flist)):
            con = Flist[i].decode('utf8').replace('\t', ' ').rstrip()
            print(i,"文件写入次数")
            manu.input_text_info_noclear(con)
        time.sleep(10)
        manu.paper_check_button()
        time.sleep(1)
        altertext= self.close_alert_and_get_its_text()
        time.sleep(1)
        self.assertEqual(altertext,"字数不得少于200,不得大于100000")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"manual_text_long.jpg")

    def test_manual_Info_ok_9(self):
        '''信息输入正确，检测成功'''
        f = FilesOption()
        g = GetPath()
        manu = ManualEntry(self.driver)
        filePath =g.getAbsoluteFilePath("success_text.txt",r"paperDetectionManu\\success_text.txt")
        Flist = f.readFileContent(filePath)
        self.ManualNoText("文本信息正确开始检测","作者")
        for i in range(0,len(Flist)):
            con = Flist[i].decode('utf8').replace('\t', '    ').rstrip()
            manu.input_text_info_noclear(con)
        time.sleep(5)
        manu.paper_check_button()
        time.sleep(1)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"manual_info_ok.jpg")

    #关闭alter 得到对应的提示信息
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

if __name__=='__main__':
    unittest.main()
