#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/10 10:14
# @Author  : Nxy
# @Site    : 
# @File    : getResultImage.py
# @Software: PyCharm
from selenium import webdriver
import os

class getResultImage():
    def insert_image(self,driver,file_name):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        base_dir = str(base_dir)
        base_dir= base_dir.replace('\\','/')
        file_path = base_dir + "/testResult/testImages/"+file_name
        # driver.save_screenshot(file_path)
        driver.get_screenshot_as_file(file_path)

if __name__=='__main__':
    s = getResultImage()
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get("http://www.baidu.com")
    s.insert_image(driver,'baidu.jpg')
    driver.quit()




