#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-28 10:01:50
# @Author  : Nxy
# @Site    : 
# @File    : userVer.py
# @Software: PyCharm
from testCase.pageObj.basePage import BasePage
from selenium.webdriver.common.by import By
from time import sleep
class UserVer(BasePage):
    #登录各个元素定位
    login_username_loc=(By.ID,"userid")
    login_password_loc=(By.ID,"password")
    login_button_loc=(By.XPATH,"/html/body/form/div[5]/div/div[1]/div[6]/input")
    user_login_success_href=(By.CSS_SELECTOR,"li.profile.single")
    logout_loc=(By.XPATH,".//*[@id='accountIdContainer']/a[3]/t")
    auto_login=(By.ID,"rememberPassword")#自动登录
    #用户登陆后提示
    uname_error_remind_loc=(By.ID,"useridError")
    # 密码为空，密码用户名错误提示均使用这个
    pwd_error_remind_loc=(By.ID,"passwordError")
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # 本科生 相似性检测 进入标志
    user_login_success_loc =(By.ID,"personAccountKey")

    def userLogin(self,username,password):
        '''
        用户登录
        :param username: 用户名
        :param password: 用户登录密码
        :return: 无返回值
        '''
        '''获取的用户名密码登录'''
        self.open("/")
        self.login_username(username)
        self.login_password(password)
        self.auto_user_login()
        self.login_button()
        sleep(5)

    def auto_user_login(self):
        self.find_element(*self.auto_login).click()
    #登录用户名
    def login_username(self,username):
        self.find_element(*self.login_username_loc).clear()
        self.find_element(*self.login_username_loc).send_keys(username)
    #登录密码
    def login_password(self,password):
        self.find_element(*self.login_password_loc).clear()
        self.find_element(*self.login_password_loc).send_keys(password)
    #登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    #用户登录成功
    def user_login_success(self):
        self.find_element(*self.user_login_success_href).click()

    #用户名错误提示
    def uname_error_remind(self):
        return self.find_element(*self.uname_error_remind_loc).text
    #密码错误提示
    def pwd_error_remind(self):
        return self.find_element(*self.pwd_error_remind_loc).text
    #登录成功后显示当前登录的用户名
    def user_login_success_verify(self):
        return self.find_element(*self.user_login_success_loc).text
    #用户退出
    def userLogout(self):
        self.find_element(*self.logout_loc).click()

    def getLoginCookie(self):
        cookie = [item["name"] + "=" + item["value"] for item in self.driver.get_cookies()]
        cookiestr = ''.join(item for item in cookie)
        return cookiestr

