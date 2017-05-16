import os

class GetPath(object):
    #获取所需文件在当前电脑中的绝对路径
    def getAbsoluteFilePath(self,file_name,file_partpath):
        """
        :param file_name: 文件全称.例："testvb.exe"
        :param file_partpath: testData下的文件路径.例：r"massProduceUploadApps\testvb.exe"
        :return:
        """
        path = os.path.abspath(file_name)
        path_dir = path.split("simily_bdcheck_student")
        absolutepath = str(path_dir[0])+r"simily_bdcheck_student\testData\%s"%(file_partpath)
        return absolutepath

    def getAbsoluteDirPath(self,file_partpath):
        """
        获取当前目录在本机的绝对路径
        :param file_partpath: testData下的文件路径.例：r"massProduceUploadApps\testvb.exe"
        :return:
        """
        path = os.path.abspath(file_partpath)
        path_dir = path.split("simily_bdcheck_student")
        absolutepath = str(path_dir[0])+r"simily_bdcheck_student\testData\%s"%(file_partpath)
        #print( "全路径为：",str(absolutepath))
        return absolutepath

if __name__ == "__main__":
    print(GetPath().getAbsoluteDirPath("downloadFiles"))
    a=GetPath().getAbsoluteFilePath("testvb.exe",r"massProduceUploadApps\testvb.exe")
    print(a)