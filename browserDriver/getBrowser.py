#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/10 17:05
# @Author  : Nxy
# @Site    : 
# @File    : getBrowser.py
# @Software: PyCharm
from selenium.webdriver import Remote
from selenium import  webdriver

#启动浏览器
#启动浏览器驱动,注意字典的传入方式
# **dc 代表可以传入多个 字典值
# def browser(host,**dc):
#     driver=Remote(command_executor='http://'+host,desired_capabilities=dc)
#     return driver

def browser():
    host='127.0.0.1'
    dc={'browserName':'firefox'}
    driver=Remote(command_executor='http://'+host,desired_capabilities=dc)
    return driver


if __name__=='__main__':
    dr=browser()
    dr.implicitly_wait(10)
    dr.get("http://www.baidu.com/")
    dr.find_element_by_id("kw").send_keys("selenium 测试")
    dr.find_element_by_id("su").click()
    dr.quit()
