#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/11/24 10:47
# @Author  : Nxy
# @Site    : 
# @File    : readExcel.py
# @Software: PyCharm
import xdrlib,sys
import xlrd
'''
主要对excel 的操作，包括excel 的读取，以及excel内容的输出
'''
class ExcelOption():
    '''
    excelPath:excel 的地址
    openExcel 主要是打开excel 文件
    '''
    def openExcel(self,excelPath):
        try:
            data = xlrd.open_workbook(excelPath)
            return data
        except Exception as e:
            print(e)
    '''
    wbook：通过openExcel 得到的excel 数据流
    sheetIndex：excel 的sheet 的下标索引从0 开始
    colnum：sheet页单元格的列号
    rownum：sheet页单元格的行号
    readExcelBySheetNum ：主要跟根据单元格的下标进行数据的读取

    '''
    def readExcelBySheetNum(self,wbook,sheetIndex,rownum,colnum):
        sh=wbook.sheet_by_index(sheetIndex)#sheet 页的下标从0 开始
        cellName = sh.cell(rownum,colnum).value #cell(行号,列号) 均是从下标0 开始
        return cellName
    '''
    wbook：通过openExcel 得到的excel 数据流
    sheetName：excel 的sheet 的name
    colnum：sheet页单元格的列号
    rownum：sheet页单元格的行号
    readExcelBySheetName ：主要跟根据单元格的名称进行数据的读取

    '''
    def readExcelBySheetName(self,wbook,sheetName,rownum,colnum):
        sh=wbook.sheet_by_name(sheetName)#sheet页的名称
        cellName = sh.cell(rownum,colnum).value #cell(行号,列号) 均是从下标0 开始
        return cellName


if __name__=='__main__':
    excelo = ExcelOption()
    print(type(excelo.openExcel("E:\Work_Python_Test\excelTest\class.xls")))
    # cell = excelo.readExcelBySheetNum(excelo.openExcel("E:\Work_Python_Test\excelTest\class.xls"),0,4,1)
    # print(cell)

    cell2 = excelo.readExcelBySheetName(excelo.openExcel("E:\Work_Python_Test\excelTest\class.xls"),"Sheet1",20,1)
    print(cell2,"通过sheetname 得到数据")
