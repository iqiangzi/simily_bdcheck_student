# 目录结构


1. browerDriver 

> 主要是用于存放浏览器驱动以及浏览器启动程序的包文件


----------


2. daoImpl 

> 主要用于存放数据库操作记录的包文件
> 

----------

3. testCase
4. -- models 对应的系统模块用例包
5. -- pageObj 对应的系统中公用的对象包

- ------systemManage（modelName即模块名）


----------

4. testData

- ------systemManage（modelName即模块名）


----------

5. testResult
6. -- testImages 用例结果截图存放包
> 主要用于存放系统测试结果

---
6. testRun

> 主要用于存放运行用例的任务


----------

7. util

- ------commonUtils（公共工具类包）
- ------dbUtil（数据库连接工具类包）
- ------toolUtils（项目中用到的工具类）


8. readHelp文件则是 系统使用说明

# 使用注意事项

1. 在idel 文件夹中 misc.xml 文件中 修改对应的project-jdk-name 为自己本机的python 版本


2. D:\Program Files\Python3.5\python.exe 即是自己本机python 的安装目录

---

    <component name="ProjectRootManager" version="2" project-jdk-name="Python 3.5.2 (D:\Program Files\Python3.5\python.exe)" 
    project-jdk-type="Python SDK" /></project>







