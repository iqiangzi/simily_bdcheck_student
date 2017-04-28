#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/02/12 9:38
# @Author  : Nxy
# @Site    :
# @File    : setBrowser.py
# @Software: PyCharm

''' 在测试中启动浏览器'''
from selenium import webdriver
from util.toolUtils.getPath import GetPath
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
class setBrowser ():

    """
    练习启动各种浏览器：Firefox， Chrome， IE
    练习启动各种浏览器的同时加载插件：Firefox， Chrome， IE
    """
    # def startFirefox (self):
    #     """这里启动firefox 有别于python2 ，需要用户自行下载驱动
    #     在地址： https://github.com/mozilla/geckodriver/releases/tag/v0.11.1
    #     将下载后的文件解压放在firefox 的安装目录下，并将firefox【 的按住那个目录配置在path中
    #     重新打开 项目即可启动firefox"""
    #     driver = webdriver.Firefox ()
    #     return driver

    def startFirefox (self,downloadPath):
        """这里启动firefox 有别于python2 ，需要用户自行下载驱动
        在地址： https://github.com/mozilla/geckodriver/releases/tag/v0.11.1
        将下载后的文件解压放在firefox 的安装目录下，并将firefox【 的按住那个目录配置在path中
        重新打开 项目即可启动firefox"""
        #实例化一个火狐配置文件
        fp = webdriver.FirefoxProfile()
        #设置各项参数，参数可以通过在浏览器地址栏中输入about:config查看。
        #设置成0代表下载到浏览器默认下载路径；设置成2则可以保存到指定目录
        #下载到指定目录
        fp.set_preference("browser.download.dir",downloadPath)
        fp.set_preference("browser.download.folderList",2)
        #不询问下载路径；后面的参数为要下载页面的Content-type的值octet-stream
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/octet-stream;text/plain;application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;application/pdf;application/msword;application/rtf")
        # fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/pdf")
        #是否显示开始,(个人实验，不管设成True还是False，都不显示开始，直接下载)
        fp.set_preference("browser.download.manager.showWhenStarting",False)
        fp.set_preference( "pdfjs.disabled", True )
        #启动一个火狐浏览器进程，以刚才的浏览器参数
        driver = webdriver.Firefox (firefox_profile=fp)
        return driver

    '''
    打开chrome浏览器
    driverPath： chrome 浏览器的驱动放置位置
    '''
    def startChrome (self, driverPath,downloadPath):
        #设置chrome自动下载到指定路径
        download_dir=GetPath().getAbsoluteDirPath(downloadPath)
        options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': downloadPath}
        options.add_experimental_option('prefs', prefs)
        driver = webdriver.Chrome (driverPath, chrome_options=options)  # 调用chrome浏览器
        return driver

    '''
    打开ie浏览器，目前win10 系统是 Microsoft Edge
    而不是ie 所以该方法在win10 不可用
    driverPath： ie 浏览器的驱动放置位置
    '''
    def startIE (self,driverPath):
        driver = webdriver.Ie (driverPath)
        return driver
if __name__ == '__main__':
    b = setBrowser ()
    # driver = b.startChromeNoUrl("E:\\PyCharm_Workspace\\TestFrame\\com\\browserDriver\\chromedriver.exe")
    # driver.get("http://www.jd.com")
    # b.getElementDisplay(driver,'xpath','//*[@id="ttbar-login"]/a[1]')
    # b.startIE("http://www.baidu.com","E:\\PyCharm_Workspace\\TestFrame\\com\\browserDriver\\IEDriverServer.exe")
    d= b.startFirefox ("downloadFiles")
    d.get("http://www.baidu.com")
   #  b.startChrome("http://www.baidu.com","E:\\PyCharm_Workspace\\TestFrame\\com\\browserDriver\\chromedriver.exe")
