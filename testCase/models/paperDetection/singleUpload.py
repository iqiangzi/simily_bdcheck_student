#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-28 10:01:50
# @Author  : Nxy
# @Site    : 
# @File    : singleUpload.py
# @Software: PyCharm
from testCase.pageObj.basePage import BasePage
from selenium.webdriver.common.by import By
from time import sleep
from util.commonUtils.upLoad import UpLoad


class SingleUpload(BasePage):
    loding_loc=(By.CLASS_NAME,"upload-text") #检测和上传 缓冲标记
    single_upload_loc=(By.CLASS_NAME,"colleupbtn")
    title_input_loc=(By.ID,"title")
    author_input_loc =(By.ID,"author")
    upload_button_loc = (By.ID,"uploadPaper")
    file_select_loc=(By.ID,"falseuploadPaper")
    paper_title_error_loc = (By.ID,"titleMessage") #标题错误信息
    paper_author_error_loc= (By.ID,"authorMessage")#作者错误信息

    #用户进行单篇上传操作
    def singleUpload(self,titleInfo,authorInfo):
        self.select_single_upload()
        self.driver.get(self.base_url + "/Check")
        self.input_title_info(titleInfo)
        sleep(3)
        self.input_author_info(authorInfo)
        print("信息已输入完毕")
        self.file_upload_button()


    #用户选择单篇上传
    def select_single_upload(self):
        self.find_element(*self.single_upload_loc).click()
    def input_title_info(self,titleInfo):
        '''
        输入标题信息
        :param titleInfo:
        :return:
        '''
        self.find_element(*self.title_input_loc).clear()
        self.find_element(*self.title_input_loc).send_keys(titleInfo)

    def input_author_info(self,authorInfo):
        '''
        输入作者信息
        :param authorInfo:
        :return:
        '''
        self.find_element(*self.author_input_loc).clear()
        self.find_element(*self.author_input_loc).send_keys(authorInfo)
    #标题必填提示信息
    def title_null_mind(self):
        return self.find_element(*self.paper_title_error_loc).text
    #作者必填提示信息
    def author_null_mind(self):
        return self.find_element(*self.paper_author_error_loc).text
    #文件上传按钮
    def file_upload_button(self):
        self.find_element(*self.upload_button_loc).click()
    #文件上传
    #上传文件方法
    def file_upload(self,filename):
        upload = UpLoad()
        upload.uploadFile_para("chrome",filename)

    #加载提示，正在上传或 正在检测
    def buffer_prompt(self):
        return self.find_element(*self.upload_button_loc).text
    #获得支付的url
    def getPayUrl(self):
        return self.driver.current_url