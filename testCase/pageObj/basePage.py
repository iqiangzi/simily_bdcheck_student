#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/13 13:25
# @Author  : Nxy
# @Site    : 
# @File    : BasePage.py
# @Software: PyCharm
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from testCase.models import myUnitFirefox
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

from util.toolUtils.getPath import GetPath


class BasePage(object):
    '''
    页面基础类，用于所有页面的继承
    '''
    #burl ="http://login.test.wanfangdata.com.cn/Login.aspx" # 万方主站所用用户登录入口
    burl ="http://check.test.wanfangdata.com.cn/md" #万方相似性硕博登录入口


    def __init__(self,selenium_driver,base_url= burl,parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    def _open(self,url):
        url = self.base_url +url
        self.driver.get(url)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    def open(self,url):
        self._open(url)

    def script(self,src):
        return self.driver.execute_script(src)
    #处理弹出窗口，注意是确认窗口
    def confirm_window(self):
        return self.driver.switch_to.alert().text
    #frame转换
    def user_login_switch(self,id):
        self.driver.switch_to.frame(id)
    #跳到最外层窗口
    def user_switch_default(self):
        self.driver.switch_to.default_content()
    #处理浏览器弹窗
    def confirm_broserAlert(self):
        alert = self.driver.switch_to_alert()
        #print(alert.text)
        text = alert.text
        alert.accept()
        return text

    def is_element_visible(self, element):
        '''
        判断某元素是否存在，存在返回true
        :param element:
        :return:
        '''
        driver = self.driver
        try:
            the_element = EC.visibility_of_element_located(element)
            assert the_element(driver)
            flag = True
        except:
            flag = False
        return flag

    def wait_element_visible(self, time, element):
        '''
        等待元素出现，超过时间页面加载失败
        :param time:
        :param element:
        :return:
        '''
        try:
            WebDriverWait(self.driver, time).until(EC.presence_of_element_located(element))
            return self.driver.find_element(*element)
        except Exception as e:
            print('元素异常, 页面已截图 :')
            self.driver.screenshot()

    #判断是否下载到本地,返回bool类型的True或False
    def verifyExist(self,fileName,filePath):
        ab_path = GetPath().getAbsoluteFilePath(fileName,filePath)
        flag = os.path.exists(ab_path)
        return flag

if __name__=='__main__':
    s = BasePage(selenium_driver=webdriver.Firefox())
    s.open("/")
    all_search_loc=(By.NAME,"btSelectAll")
