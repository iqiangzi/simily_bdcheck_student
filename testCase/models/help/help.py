#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-28 10:01:50
# @Author  : Nxy
# @Site    : 
# @File    : help.py
# @Software: PyCharm
from selenium import  webdriver
import unittest

from selenium.webdriver.common.by import By

from testCase.pageObj.basePage import BasePage
import time

class Help(BasePage):
         #帮助模块
    help_button_loc=(By.ID,"help")
    account_manage_loc=(By.ID,"accountInfo")

    def enter_account_manage(self):
        self.find_element(*self.account_manage_loc).click()

    def enterManage(self,headers):
        self.enter_account_manage()
        self.driver.get(self.base_url + "/Manage")


    def enter_help(self,headers):
        self.in_help()
        self.driver.get(self.base_url + "/Help")

    def in_help(self):
        self.find_element(*self.help_button_loc).click()
