#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-28 10:01:50
# @Author  : Nxy
# @Site    : 
# @File    : manualEntry.py
# @Software: PyCharm
from selenium import  webdriver
import unittest

from selenium.webdriver.common.by import By

from testCase.pageObj.basePage import BasePage
import time

class ManualEntry(BasePage):
    hand_made_loc=(By.CLASS_NAME,"colleManualbtn")
    title_input_loc=(By.ID,"title")
    author_input_loc =(By.ID,"author")
    nocheck_button_loc = (By.ID,"disableCheck")
    check_button_loc = (By.ID,"check")
    text_input_loc=(By.ID,"content")

    paper_title_error_loc = (By.ID,"titleMessage") #标题错误信息
    paper_author_error_loc= (By.ID,"authorMessage")#作者错误信息
    paper_text_error_loc=(By.ID,"textMessage")#文本错误


    #用户开始手工检测
    def manualEntryOption(self,titleInfo,authorInfo,textInfo):
        self.enter_handmade()
        self.driver.get(self.base_url + "/ManualCheck")
        self.input_title_info(titleInfo)
        self.input_author_info(authorInfo)
        self.input_text_info(textInfo)
        time.sleep(10)
        if(self.is_not_visible(2,self.nocheck_button_loc)==False):
            pass
        else:
            self.paper_check_button()

    #用户开始手工检测
    def manualEntry(self,titleInfo,authorInfo):
        self.enter_handmade()
        self.driver.get(self.base_url + "/ManualCheck")
        self.input_title_info(titleInfo)
        self.input_author_info(authorInfo)

    def enter_handmade(self):
         self.find_element(*self.hand_made_loc).click()

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
    def input_text_info(self,textInfo):
        '''
        输入检测文本信息
        :param textInfo:
        :return:
        '''
        self.find_element(*self.text_input_loc).clear()
        self.find_element(*self.text_input_loc).send_keys(textInfo)
    def input_text_info_noclear(self,textInfo):
        '''
        不对文本框进行清空，输入检测文本信息
        :param textInfo:
        :return:
        '''
        self.find_element(*self.text_input_loc).send_keys(textInfo)
    #文本必填提示信息
    def text_null_mind(self):
        return self.find_element(*self.paper_text_error_loc).text
    #标题必填提示信息
    def title_null_mind(self):
        return self.find_element(*self.paper_title_error_loc).text
    #作者必填提示信息
    def author_null_mind(self):
        return self.find_element(*self.paper_author_error_loc).text
    #开始检测按钮
    def paper_check_button(self):
        self.find_element(*self.check_button_loc).click()

