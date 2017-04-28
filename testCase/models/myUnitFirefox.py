#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/13 13:25
# @Author  : Nxy
# @Site    : 
# @File    : MyUnit.py
# @Software: PyCharm
from browserDriver.setBrowser import setBrowser
import unittest
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from util.toolUtils.getPath import GetPath


class UnitFirefox(unittest.TestCase):
    def setUp(self):
        s= setBrowser()
        download_dir=GetPath().getAbsoluteDirPath("downloadFiles")
        self.driver=s.startFirefox(download_dir)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True
    def tearDown(self):
        self.driver.quit()

#
# if __name__=='__main__':
#     t = UnitFirefox()
#     d = t.setUp()
#     d.get("http://www.baidu.com")

