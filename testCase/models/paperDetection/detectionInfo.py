#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/8 16:39
# @Author  : Nxy
# @Site    : 
# @File    : detectionInfo.py
# @Software: PyCharm
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from testCase.pageObj.basePage import BasePage

class DetectionInfo(BasePage):
    fulltext_reportV1_loc=(By.XPATH,"(//a[contains(text(),'V1.0')])[2]")
    detail_download_reportV1_loc=(By.LINK_TEXT,"V1.0")
    detail_download_reportV2_loc=(By.LINK_TEXT,"V2.0")

    option_loc=(By.LINK_TEXT,u"重新检测")#操作

    pageNum="2"
    page_num_loc=(By.LINK_TEXT,pageNum)
    #翻页到指定页码
    def gotoPageNum(self,pageNum):
        self.find_element(*self.page_num_loc).click()
    pageSize="20"
    page_down_loc=(By.ID,"sel")
    page_size_loc=(By.LINK_TEXT,pageSize)
    #设置每页显示条数
    def gotoPageSize(self,pageSize):
        Select(self.find_element(*self.page_down_loc)).select_by_visible_text(pageSize)

    #详细报告下载
    def detection_detail_download(self):
        ele_flag = self.is_element_visible(self.option_loc)
        if ele_flag==True:
            self.option_detection()
        else:
            v2_flag = self.is_element_visible(self.detail_download_reportV2_loc)
            if(v2_flag==True):
                self.detail_v2_down()
                time.sleep(2)
                self.detail_v1_down()
            else:
                self.detail_v1_down()
                print("v2.0检测失败")
    #全文进行在线查看
    def detection_fulltext_look(self):
        ele_flag = self.is_element_visible(self.option_loc)
        if ele_flag==True:
            self.option_detection()
        else:
            self.full_v1_look()

    def full_v1_look(self):
        self.find_element(*self.fulltext_reportV1_loc).click()

    def detail_v1_down(self):
        self.find_element(*self.detail_download_reportV1_loc).click()

    def detail_v2_down(self):
        self.find_element(*self.detail_download_reportV2_loc).click()

    def option_detection(self):
        self.find_element(*self.option_loc).click()
