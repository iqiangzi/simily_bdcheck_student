from util.toolUtils.getPath import GetPath
import os

class UpLoad(object):

    #调用autoit生成的exe，并传入浏览器、需要上传至页面文件的地址两个参数
    def uploadFile_para(self,browserName,filePath):
        ab_path = GetPath().getAbsoluteFilePath("testvb.exe",r"massProduceUploadApps\testvb.exe")
        #os.system("./../testData/massProduceUploadApps/testvb.exe"+ " "+browserName+" "+filePath)
        os.system(ab_path+ " "+browserName+" "+filePath)

    #获取上传文件的绝对路径
    def getFilePath(self,dirname,filename):
        '''
        文件上传测试
        :param dirname: testData目录下各个模块数据文件夹的名称
        :param filename: 需要获得绝对路径文件的名称
        :return:
        '''
        file_path = GetPath().getAbsoluteFilePath("%s"%filename,r"%s\%s"%(dirname,filename))
        return file_path