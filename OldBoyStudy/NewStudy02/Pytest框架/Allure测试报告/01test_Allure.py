# -*- coding: utf-8 -*-
# @Time : 2021/11/27 15:47
# @Author : huix
# @File : 01test_Allure.py

"""
Allure介绍

allure是一个灵活的、轻量级的、支持多语言的测试报告工具
- 多平台的，奢华的report框架
- 可以为dev/QA提供详细的测试报告、测试步骤、log等
- 也可以为管理层提供high level统计报告
- 是用JAVA语言开发的，支持pytest、JavaScript、PHP、Ruby等
- 可以集成到Jenkins
- 官网：http://allure.qatools.ru/

如何安装
windows：
- github安装——》解压——》进入bin目录——》运行allure.bat
- 把bin目录加入到PATH环境变量里面去
- 或者scoop install allure

mac：
- brew install allure
安装pytest-allure
- pip install pytest-allure
如果在pycharm中执行，需要在pycharm里面安装allure-pytest插件


执行命令生成测试报告：(生成的是json报告)
- pytest 02test_Allure2.py --alluredir=./reports
- python -m pytest 02test_Allure2.py --alluredir=./reports/7

展示测试报告（根据生成的json文件打开一个html报告）
- allure serve ./reports(报告路径)

第二种方式（会生成一个html的测试报告）
- allure generate ./reports/7 -o ./reports/7/html
- allure open -h 127.0.0.1 -p 8883 ./reports/7/html

"""


"""
03test_AllureDemo.py

features特性：
- 只执行结算模块的测试用例
- pytest test_a.py --allure-features=“结算模块” -vs

只执行结算模块第二条用例
- pytest test_a.py --allure-stories=“结算模块第二条用例” -vs

链接到测试管理的地址（例如tapd平台，禅道等）
- allure.testcase("http://tapd.oa.com")

在测试报告中加入一个测试用例的链接地址，这里我们使用https://www.baidu.com/为例
- @allure.link("www.baidu.com")


按照重要性级别进行一定范围测试
- 级别：Trivial-不重要 Minor不太重要 Normal 正常问题 Critical严重 Blocker：阻塞
- 在方法函数和类上面加@allure.severity(allure.severity_level.TRIVIAL)
- 执行时 pytest -s -v 文件名 --allure-severities="normal,critical"
# argument --allure-severities: Illegal severity values: CRTICAL, NORMAL, only [critical, trivial, minor, blocker, normal] are allowed

我们希望不适用方法名命名我们的测试报告的标题，也就是如图所示的位置
- @allure.title("加购模块第一条用例")

可以在每条测试用例前加上测试步骤的说明
- with allure.step("登陆")
- with allure.step("搜索)

在测试报告里面加上截图跟视频
- allure.attach.file("1.jpg", name = "这是截图", attachment_type=allure.attachment_type.JPG)
- allure.attach.file("jue.mp4", name = "这是一个视频", attachment_type=allure.attachment_type.MP4)

"""