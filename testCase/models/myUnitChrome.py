#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/7 17:48
# @Author  : Nxy
# @Site    : 
# @File    : myUnitChrome.py
# @Software: PyCharm
from selenium import webdriver
from browserDriver.setBrowser import setBrowser
import unittest
from util.toolUtils.getPath import GetPath


class UnitChrome(unittest.TestCase):
    def setUp(self):
        s= setBrowser()
        download_dir=GetPath().getAbsoluteDirPath("downloadFiles")
        self.driver=s.startChrome("../browserDriver/chromedriver.exe",download_dir)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        # pass
        self.driver.quit()

if __name__=='__main__':
    t = UnitChrome()
    d = t.setUp()
    d.get("http://www.baidu.com")

