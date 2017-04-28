#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/23 14:30
# @Author  : Nxy
# @Site    : 
# @File    : getAllCasesReport.py
# @Software: PyCharm
import unittest,time
from HTMLTestRunner import  HTMLTestRunner

#指定测试用例为当前文件夹下的test_case 目录

class GetAllCasesReport():

    def createReport(self,test_report_dir,test_case_dir,report_name,report_title,report_desc):
        """
        :param test_report_dir: 测试报告存放目录
        :param test_case_dir: 执行测试用例目录
        :param report_name: 报告名称
        :param report_title: 报告主题
        :param report_desc: 报告描述
        :return:
        """
        discover = unittest.defaultTestLoader.discover(test_case_dir,pattern='run_*.py')
        fp= open(report_name,'wb')
        # 定义测试报告
        runner = HTMLTestRunner(stream=fp,title=report_title,description=report_desc)
        runner.run(discover) #运行测试用例
        fp.close()#关闭报告文件

if __name__=='__main__':
    t = GetAllCasesReport()
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    test_report_dir = '../testResult'
    test_case_run_dir ='../testRun'
    print("现在时间是"+now)
    # 定义报告存放路径
    filename = test_report_dir+'/'+ now +'_result.html'
    t.createReport(test_report_dir,test_case_run_dir,filename,'测试报告', '测试执行情况：')
