#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-28 10:01:50
# @Author  : Nxy
# @Site    : 
# @File    : run_accountMgmt.py
# @Software: PyCharm
from selenium import  webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from testCase.models import myUnitChrome
from testCase.models import myUnitFirefox
from testCase.models.accountMgmt.accountMgmt import AccountMgmt
from testCase.models.userVer.userVer import UserVer
from testResult.getResultImage import getResultImage


class RunAccountMgmt(myUnitChrome.UnitChrome):
    def user_login(self):
        '''用户登录'''
        user_login = UserVer(self.driver)
        user_login.userLogin(username="collegecheck.student2233",password="123456")

    def ModifyPwdOption(self,newpwd,repwd):
        self.user_login()
        time.sleep(2)
        accm = AccountMgmt(self.driver)
        accm.modifyPassword(newpwd,repwd)

    def UserEnterMange(self):
        self.user_login()
        time.sleep(2)
        accm = AccountMgmt(self.driver)
        accm.enterManage()

    def test_myWallet_info_1(self):
        '''查看充值链接是否正确'''
        self.UserEnterMange()
        accm = AccountMgmt(self.driver)
        self.assertEqual(accm.chongzhi_info(),"http://tran.test.wanfangdata.com.cn/Charge.aspx")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"chongzhi_href_ok.jpg")

    def test_myAccount_info_2(self):
        '''查看账户信息是否为当前登录用户'''
        self.UserEnterMange()
        accm = AccountMgmt(self.driver)
        self.assertEqual(accm.look_account_info(),accm.login_info())
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"userinfo_right_ok.jpg")

    def test_modifyPassword_type_error_3(self):
        '''修改密码，密码格式不正确'''
        newp = "1"
        repwd="1"
        self.ModifyPwdOption(newp,repwd)
        accm = AccountMgmt(self.driver)
        self.assertEqual(accm.pwd_error_mind(),"密码格式不正确")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"pwd_type_error.jpg")

    def test_modifyPassword_nosame_4(self):
        '''两次密码输入不一样'''
        newp = "123456"
        repwd="12345678"
        self.ModifyPwdOption(newp,repwd)
        accm = AccountMgmt(self.driver)
        self.assertEqual(accm.pwd_error_mind(),"两次输入密码必须一致")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"pwd_no_same.jpg")

    def test_modifyPassword_null_5(self):
        '''必填信息为空'''
        newp = ""
        repwd=""
        self.ModifyPwdOption(newp,repwd)
        accm = AccountMgmt(self.driver)
        self.assertEqual(accm.pwd_error_mind(),"必填项皆不能为空。")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"pwd_null.jpg")

    def test_modifyPassword_ok_5(self):
        '''密码修改成功'''
        newp = "123456"
        repwd="123456"
        self.ModifyPwdOption(newp,repwd)
        time.sleep(2)
        alterText = self.close_alert_and_get_its_text()
        time.sleep(2)
        self.assertEqual(alterText,"修改密码成功，请重新登录")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"pwd_ok.jpg")

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