#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/10 9:19
# @Author  : Nxy
# @Site    : 
# @File    : payOption.py
# @Software: PyCharm
from testCase.models.paperDetection.singleUpload import SingleUpload
from testCase.pageObj.basePage import BasePage
from selenium.webdriver.common.by import By
from time import sleep

from util.commonUtils.upLoad import UpLoad


class PayOption(BasePage):
    pay_ali_loc=(By.ID,"to_AlipayConfirm")#阿里支付宝支付
    pay_union_loc=(By.ID,"to_UnionPayConfirm")#银联支付
    other_user_login_loc=(By.ID,"loginBtn")#其他用户登录
    chongzhi_loc=(By.CLASS_NAME,"link2")#充值链接
    other_login_div =(By.XPATH,"html/body/div[2]")#其他用户登陆框

    def detection_input(self,titleInfo,authorInfo,filename):
        su = SingleUpload(self.driver)
        su.select_single_upload()
        self.driver.get(self.base_url + "/Check")
        su.input_title_info(titleInfo)
        sleep(3)
        su.input_author_info(authorInfo)
        print("信息已输入完毕")
        su.file_upload_button()
        upload = UpLoad()
        upload.uploadFile_para("chrome",filename)

    def user_mywallet_pay(self,username,titleInfo,authorInfo,filename):
        self.detection_input(titleInfo,authorInfo,filename)
        sleep(5)
        self.pay_mywallet(username)
        sleep(3)

    username = "collegecheckstudent2233"
    pay_mywallet_loc=(By.ID,"to_Person" + username +"Confirm")#钱包支付

    #我的钱包支付
    def pay_mywallet(self,username):
        self.find_element(*self.pay_mywallet_loc).click()
    #阿里支付
    def pay_ali(self):
        self.find_element(*self.pay_ali_loc).click()
    #银联支付
    def pay_union(self):
        self.find_element(*self.pay_union_loc).click()
    #其他用户登录
    def other_user_login(self):
        self.find_element(*self.other_user_login_loc).click()
    #充值
    def chongzhi(self):
        self.find_element(*self.chongzhi_loc).click()

    def login_div(self):
        divFlag = self.is_element_visible(self.other_login_div)
        if(divFlag==True):
            return "其他用户登录div存在"
        else:
            return "其他用户登录div 不存在"
