#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-28 10:01:50
# @Author  : Nxy
# @Site    : 
# @File    : run_singleUpload.py
# @Software: PyCharm
from selenium import  webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from testCase.models import myUnitChrome
from testCase.models import myUnitFirefox
from testCase.models.paperDetection.singleUpload import SingleUpload
from testCase.models.userVer.userVer import UserVer
from testResult.getResultImage import getResultImage
from util.commonUtils.upLoad import UpLoad
from util.toolUtils.getPath import GetPath


class RunSingleUpload(myUnitChrome.UnitChrome):
    def user_login(self):
        '''用户登录'''
        user_login = UserVer(self.driver)
        user_login.userLogin(username="collegecheck.student2233",password="123456")
    #单篇上传
    def singleUploadOption(self,titleInfo,authorInfo):
        self.user_login()
        sut =SingleUpload(self.driver)
        sut.singleUpload(titleInfo,authorInfo)

    def test_testInfo_null_run_1(self):
        '''标题，作者信息为空，无法上传论文'''
        sut =SingleUpload(self.driver)
        self.singleUploadOption("","")
        self.assertEqual(sut.title_null_mind(),"请输入题名")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"single_info_null.jpg")

    def test_title_null_run_2(self):
        '''标题信息为空，无法上传论文'''
        sut =SingleUpload(self.driver)
        self.singleUploadOption("","测试")
        self.assertEqual(sut.title_null_mind(),"请输入题名")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"single_title_null.jpg")


    def test_author_null_run_3(self):
        '''作者信息为空，无法上传论文'''
        sut =SingleUpload(self.driver)
        self.singleUploadOption("测试信息","")
        self.assertEqual(sut.author_null_mind(),"请输入作者")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"single_author_null.jpg")

    def test_title_long_run_4(self):
        '''标题信息超过规定的50，无法上传论文'''
        sut =SingleUpload(self.driver)
        titleInfo="123456789测试信息测试信息测试信息测试信息测试信测试信息测试信息测试信息测试信息测试信息测试信息息"
        self.singleUploadOption(titleInfo,"测试")
        time.sleep(3)
        altertxt = self.close_alert_and_get_its_text()
        time.sleep(2)
        self.assertEqual("题名长度不得大于50",altertxt)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"single_title_long.jpg")

    def test_author_long_run_5(self):
        '''作者信息超过规定的50，无法上传论文'''
        sut =SingleUpload(self.driver)
        authorInfo="123456789测试信息测试信息测试信息测试信息测试信测试信息测试信息测试信息测试信息测试信息测试信息息"
        self.singleUploadOption("测试信息",authorInfo)
        time.sleep(2)
        altertxt = self.close_alert_and_get_its_text()
        time.sleep(2)
        self.assertEqual(altertxt,"作者长度不得大于50")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"single_author_null.jpg")
    def test_file_empty_run_6(self):
        '''空文件，无法上传论文'''
        sut =SingleUpload(self.driver)
        self.singleUploadOption("空文件","测试")
        filePath = GetPath().getAbsoluteFilePath("0kb.txt","pDeteSingleUpload\\0kb.txt")
        time.sleep(1)
        sut.file_upload(filePath)
        time.sleep(2)
        altertxt = self.close_alert_and_get_its_text()
        time.sleep(2)
        self.assertEqual("上传失败，文件为空!",altertxt)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"single_text_empty.jpg")

    def test_file_type_wrong_run_7(self):
        '''文件格式不支持，无法上传论文'''
        sut =SingleUpload(self.driver)
        self.singleUploadOption("文件格式不是规定范围内","测试")
        filePath = GetPath().getAbsoluteFilePath("1.jpg","pDeteSingleUpload\\1.jpg")
        time.sleep(1)
        sut.file_upload(filePath)
        # sut.buffer_prompt()
        time.sleep(2)
        altertxt = self.close_alert_and_get_its_text()
        time.sleep(2)
        self.assertEqual("上传失败，文件为空!",altertxt)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"single_filetype_wrong.jpg")

    def test_file_small_run_8(self):
        '''文档字数受限,文档字数为200至1000000，无法上传论文'''
        sut =SingleUpload(self.driver)
        self.singleUploadOption("文本信息字数过少","测试")
        filePath = GetPath().getAbsoluteFilePath("199Words.txt","pDeteSingleUpload\\199Words.txt")
        time.sleep(1)
        sut.file_upload(filePath)
        sut.buffer_prompt()
        time.sleep(3)
        altertxt = self.close_alert_and_get_its_text()
        time.sleep(2)
        self.assertEqual("文档字数受限,文档字数为200至1000000",altertxt)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"single_text_small.jpg")

    def test_file_big_run_9(self):
        '''文档字数受限,文档字数为200至1000000，无法上传论文'''
        sut =SingleUpload(self.driver)
        self.singleUploadOption("文本信息字数过多","测试")
        filePath = GetPath().getAbsoluteFilePath("big_text.txt","pDeteSingleUpload\\big_text.txt")
        time.sleep(1)
        sut.file_upload(filePath)
        sut.buffer_prompt()
        time.sleep(10)
        altertxt = self.close_alert_and_get_its_text()
        time.sleep(2)
        self.assertEqual("文档字数受限,文档字数为200至1000000",altertxt)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"single_text_big.jpg")

    def test_filesize_big_run_10(self):
        '''文件超过规定的30M，无法上传论文'''
        sut =SingleUpload(self.driver)
        self.singleUploadOption("文件超过30M","测试")
        filePath = GetPath().getAbsoluteFilePath("BIG30M.pdf","pDeteSingleUpload\\BIG30M.pdf")
        time.sleep(1)
        sut.file_upload(filePath)
        sut.buffer_prompt()
        time.sleep(5)
        altertxt = self.close_alert_and_get_its_text()
        time.sleep(2)
        self.assertEqual("上传失败，文件过大!",altertxt)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"single_size_big.jpg")

    def test_file_content_wrong_run_11(self):
        '''不是纯文字信息，抽取失败'''
        sut =SingleUpload(self.driver)
        self.singleUploadOption("带图片及表格文件","测试")
        filePath = GetPath().getAbsoluteFilePath("content_wrong.doc","pDeteSingleUpload\\content_wrong.doc")
        time.sleep(1)
        sut.file_upload(filePath)
        sut.buffer_prompt()
        time.sleep(10)
        altertxt = self.close_alert_and_get_its_text()
        time.sleep(2)
        self.assertEqual("文本抽取失败，请重新上传",altertxt)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"single_content_fail.jpg")

    def test_file_doc_ok_run_12(self):
        '''上传合格的doc文件，上传成功'''
        sut =SingleUpload(self.driver)
        self.singleUploadOption("doc文件","测试")
        filePath = GetPath().getAbsoluteFilePath("general_doc_OK.doc","pDeteSingleUpload\\general_doc_OK.doc")
        time.sleep(1)
        sut.file_upload(filePath)
        sut.buffer_prompt()
        time.sleep(10)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"single_doc_ok.jpg")
    def test_file_docx_ok_run_13(self):
        '''上传合格的docx文件，上传成功'''
        sut =SingleUpload(self.driver)
        self.singleUploadOption("docx文件","测试")
        filePath = GetPath().getAbsoluteFilePath("general_DOCX_OK.docx","pDeteSingleUpload\\general_DOCX_OK.docx")
        time.sleep(1)
        sut.file_upload(filePath)
        sut.buffer_prompt()
        time.sleep(10)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"single_docx_ok.jpg")
    def test_file_pdf_ok_run_14(self):
        '''上传合格的pdf文件，上传成功'''
        sut =SingleUpload(self.driver)
        self.singleUploadOption("pdf文件","测试")
        filePath = GetPath().getAbsoluteFilePath("PDF_OK.pdf","pDeteSingleUpload\\PDF_OK.pdf")
        time.sleep(1)
        sut.file_upload(filePath)
        sut.buffer_prompt()
        time.sleep(10)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"single_pdf_ok.jpg")
    def test_file_rtf_ok_run_15(self):
        '''上传合格的rtf文件，上传成功'''
        sut =SingleUpload(self.driver)
        self.singleUploadOption("rtf文件","测试")
        filePath = GetPath().getAbsoluteFilePath("general_RTF_OK.rtf","pDeteSingleUpload\\general_RTF_OK.rtf")
        time.sleep(1)
        sut.file_upload(filePath)
        sut.buffer_prompt()
        time.sleep(10)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"single_rtf_ok.jpg")

    def test_file_txt_ok_run_16(self):
        '''txt文档上传成功'''
        sut =SingleUpload(self.driver)
        self.singleUploadOption("txt上传成功","测试")
        filePath = GetPath().getAbsoluteFilePath("200Words.txt","pDeteSingleUpload\\200Words.txt")
        time.sleep(1)
        sut.file_upload(filePath)
        time.sleep(4)
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"single_text_ok.jpg")

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