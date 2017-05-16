#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-28 10:01:50
# @Author  : Nxy
# @Site    : 
# @File    : accountMgmt.py
# @Software: PyCharm
from selenium import  webdriver
import unittest

from selenium.webdriver.common.by import By

from testCase.pageObj.basePage import BasePage
import time

class AccountMgmt(BasePage):
    account_manage_loc=(By.ID,"accountInfo")
    account_info_loc=(By.XPATH,".//*[@id='accountIdSpan']")
    name_info_loc =(By.XPATH,"author")
    chongzhi_href=(By.XPATH,"html/body/div[4]/div[2]/div/div[4]/a")
    new_pwd_loc = (By.ID,"userpwd")
    re_pwd_loc = (By.ID,"repwd")
    modify_pwd_button_loc = (By.ID,"changePassowrdConfirm")
    info_error_loc=(By.ID,"validateTips-updatePassword")
    login_info_loc=(By.ID,"personAccountKey")

    def enterManage(self):
        self.enter_account_manage()
        self.driver.get(self.base_url + "/Manage")

    #用户修改密码操作
    def modifyPassword(self,newpwd,repwd):
        self.enterManage()
        self.new_pwd_input(newpwd)
        self.re_pwd_input(repwd)
        self.modify_pwd_button()

    def login_info(self):
        return self.find_element(*self.login_info_loc).text
    def enter_account_manage(self):
        self.find_element(*self.account_manage_loc).click()

    def look_account_info(self):
        return self.find_element(*self.account_info_loc).text

    def look_name_info(self):
        return self.find_element(*self.name_info_loc).text

    def chongzhi_info(self):
        return self.find_element(*self.chongzhi_href).get_attribute("href")

    def new_pwd_input(self,newpwd):
        self.find_element(*self.new_pwd_loc).clear()
        self.find_element(*self.new_pwd_loc).send_keys(newpwd)

    def re_pwd_input(self,repwd):
        self.find_element(*self.re_pwd_loc).clear()
        self.find_element(*self.re_pwd_loc).send_keys(repwd)

    def modify_pwd_button(self):
        self.find_element(*self.modify_pwd_button_loc).click()

    def pwd_error_mind(self):
        return self.find_element(*self.info_error_loc).text

