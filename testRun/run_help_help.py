#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-28 10:01:50
# @Author  : Nxy
# @Site    : 
# @File    : run_help.py
# @Software: PyCharm

import time
import urllib.request
from testCase.models import myUnitChrome
from testCase.models.help.help import Help
from testCase.models.userVer.userVer import UserVer
from testResult.getResultImage import getResultImage

class RunHelp(myUnitChrome.UnitChrome):

    def autoLofin(self):
        u = UserVer(self.driver)
        homeurl = self.driver.current_url
        print("当前登陆地址"+homeurl)
        cookiestr= u.getLoginCookie()
        print(cookiestr)
        headers = {'cookie':cookiestr}
        req = urllib.request.Request(homeurl, headers = headers)
        try:
            response = urllib.request.urlopen(req)
            text = response.read()
            print("得到的结果信息",text)
            fd = open('E:\\PyCharm_Workspace\\simily_bdcheck_student\\testData\\homepage.html','wb')
            fd.write(text)
            fd.close()
            print ('###get home page html success!!')
        except:
            print ('### get home page html error!!')

    def test_cookie(self):
        self.user_login()
        self.autoLofin()


    def user_login(self):
        '''用户登录'''
        user_login = UserVer(self.driver)
        user_login.userLogin(username="collegecheck.student2233",password="123456")

    def test_help_enter_1(self):
        '''用户成功进入帮助页面'''
        self.user_login()
        time.sleep(2)
        #切换到帮助页面
        cam=Help(self.driver)
        cam.enter_help()
        time.sleep(2)
        #获取页面截图
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"childAccount_help.jpg")



