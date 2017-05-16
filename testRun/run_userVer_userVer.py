#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-28 10:01:50
# @Author  : Nxy
# @Site    : 
# @File    : run_userVer.py
# @Software: PyCharm
import unittest
import time
from testCase.models import myUnitChrome
from testCase.models.userVer.userVer import UserVer
from testResult.getResultImage import getResultImage
from time import sleep
import random
class RunUserVer(myUnitChrome.UnitChrome):

    def user_login_verify_run(self,username,password):
        '''
        用户登录用例运行
        :param username: 用户名
        :param password: 密码
        :return:
        '''
        #print ("获取当前句柄",self.driver.current_window_handle)
        UserVer(self.driver).userLogin(username,password)

    def test_login_userpwdNull_run(self):
        '''用户名、密码为空登录'''
        time.sleep(2)
        self.user_login_verify_run("","")
        userver=UserVer(self.driver)
        self.assertEqual(userver.uname_error_remind(),"用户名不能为空")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"user_pwd_empty.jpg")
    def test_login_pwdNull_run(self):
        '''用户名正确，密码为空登录'''
        time.sleep(2)
        self.user_login_verify_run('collegecheck.student2233',"")
        userver=UserVer(self.driver)
        self.assertEqual(userver.pwd_error_remind(),"密码不能为空")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"pwd_empty.jpg")
    def test_login_userNull_run(self):
        '''用户名为空，密码正确'''
        time.sleep(2)
        self.user_login_verify_run(username="",password="f")
        userver=UserVer(self.driver)
        self.assertEqual(userver.uname_error_remind(),"用户名不能为空")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"uname_empty.jpg")
    def test_login_error_run(self):
        '''用户名与密码不匹配'''
        time.sleep(2)
        character=random.choice('123456rtyhj')
        username="collegecheck.student2233"+character
        self.user_login_verify_run(username,"f")
        po=UserVer(self.driver)
        self.assertEqual(po.pwd_error_remind(),"用户名或密码不正确!")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"uname_pwd_error.jpg")
    def test_login_success_run(self):
        '''用户名，密码正确'''
        self.user_login_verify_run(username="collegecheck.student2233",password="123456")
        sleep(2)
        userver=UserVer(self.driver)
        coo = userver.getLoginCookie()
        print(coo)
        self.assertEqual(userver.user_login_success_verify(),"collegecheck.student2233")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"user_login_ok.jpg")

    def test_logout_run(self):
        self.user_login_verify_run(username="collegecheck.student2233",password="123456")
        sleep(1)
        userver=UserVer(self.driver)
        userver.userLogout()
        sleep(1)

if __name__=="__main__":
    unittest.main()
