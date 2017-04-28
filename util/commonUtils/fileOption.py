#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/7 15:04
# @Author  : Nxy
# @Site    : 
# @File    : fileOption.py
# @Software: PyCharm
import os

class FilesOption():
    def getFileSize(self,fileName):
        '''
        获取文件的大小
        :param fileName: 文件名称
        :return: 返回文件的大小 ，结果为四舍五入
        '''
        file = open(fileName, 'rb')
        file.seek(0, os.SEEK_END)
        fileLength = file.tell()
        file.seek(0, 0)
        return round(fileLength/1024)

    def checkFileName(self,origFileName):
        '''
        检查文件是否已存在，如果已存在则将当前文件重命名，保证文件名的唯一
        :param origFileName:
        :return:
        '''
        finalFileName = ""
        if(origFileName.find(".")>0):
            extensionIndex = origFileName.rindex(".")
            name = origFileName[:extensionIndex]
            extension = origFileName[extensionIndex+1:]
            index = 1
            newNameSuffix = "(" + str(index) + ")"
            finalFileName = origFileName
            if os.path.exists(finalFileName):
                finalFileName = name + " " + newNameSuffix + "." + extension
            while os.path.exists(finalFileName):
                index += 1
                oldSuffix = newNameSuffix
                newNameSuffix = "(" + str(index) + ")"
                finalFileName = finalFileName.replace(oldSuffix, newNameSuffix)
        else:
            print("不是文件")
        return finalFileName


    def checkIsFile(self,FileName):
        '''
        判断该文件是文件还是文件夹，还是其他
        :param FileName:
        :return: 返回该文件的类型
        '''
        finalFileType = None
        existsFlag= os.path.exists(FileName)
        if(existsFlag == True):
            if(FileName.find(".")>0):
                fileType = os.path.isfile(FileName)
                if(fileType == True):
                    finalFileType = FileName.split(".")[1]
            else:
                dirType = os.path.isdir(FileName)
                if(dirType== True):
                    finalFileType =  "文件夹"
                else:
                    finalFileType = None
        else:
            print("文件不存在")
        return finalFileType

    def getFileList(self,startPath,fileList):
        '''
        批量获取某个目录下所有文件
        :param startPath:传入的路径
        '''
        self.startPath = startPath
        for (dirPath,dirs,files) in os.walk(startPath):
            for filename in files:
                if (len(files)>0):
                    fullFilePath = os.path.join(dirPath,filename)
                    fileList.append(fullFilePath)
        return fileList

    def readFileContent(self,fileName):
        self.fileName = fileName
        file_object = open(fileName,"rb")
        try:
            all_the_text = file_object.readlines()
            return all_the_text
        finally:
            file_object.close( )


if __name__=='__main__':
    t = FilesOption()
    # print(t.getFileSize("E:/Work_Python_Test/test.txt"))
    Flist= t.readFileContent("E:/PyCharm_Workspace/simily_shuobo/testData/paperDetectionEntry/big_text.txt")
    print(type(Flist))
    # fileContent = ';'.join(Flist)
    # print(fileContent)
    flnew =[]
    for f in Flist:
        f = f.decode('utf8')
        flnew.append(f)
        print(''.join(flnew))

    # print(t.checkFileName("E:/Work_Python_Test/test.txt"))
    # ll =[]
    # ll = t.getFileList("E:/Work_Python_Test/zipTest/2014",ll)
    # for l in ll:
    #     print(l)
    # print(t.checkIsFile("E:/Work_Python_Test/test.txt"))