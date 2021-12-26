# -*- coding: utf-8 -*-
# @Time : 2021/12/5 23:20
# @Author : huix
# @File : 01App自动化测试.py


"""
Appium是一个移动端的自动化测试框架、可用于测试原生应用，移动网页应用和混合应用，且是跨平台的。
可用于Android和iOS系统

- 跨语言：java、python、nodejs等
- 跨平台：Android/ios   Windows/Mac
- 底层是多引擎可切换
- 生态丰富，社区强大

appium环境安装
- adb
- appium Desktop
- Appium Server
- Appium client
- Appcrawler自动化遍历工具

java1.8 ver      官网下载，并配置环境变量
AndroidSDK       tools.android-stuido.org 网页下载后选择readme文件里面的命令更新版本
Node js(>=10版本)，npm（>=6）
Python3
Appium-desktop   官网或git上下载
Appium python client    通过pip install appium-python-client安装

通过appium-doctor来检测环境安装情况，需要先通过cnpm install appium-doctor安装appium-doctor工具
"""


"""
-如何获取appPackage和activityty
获取任务列表:adb shell dumpsys activity activities
获取appPackage和appActivity：adb logcat | grep -i displayed
在当前页面，获取appPackage和appActivity ： adb shell dumpsys window | grep mCurrent

-解决在新版appium客户端启动会话报错无法创建会话的问题
Remote Path需要改成"/wd/hub"

-启动appium报错没有导出ANDROID_HOME和ANDROID_SDK_ROOT环境变量
启动appium-server时先在config中配置ANDROID_HOME跟JAVA_HOME

-启动appium会话在设备安装appiumsetting后爆了一堆错：
Error: Cannot verify the signature of '/Applications/Appium Server GUI.app/Contents/Resources/app/node_modules/appium
/node_modules/appium-uiautomator2-server/apks/appium-uiautomator2-server-v4.24.0.apk'. Original error: Error: A JNI error has occurred

遇到类似的情况，是因为缺少appium-uiautomator2-server-v4.21.1.apk
试一试：在appium 安装目录下执行命令：npm install appium-uiautomator2-driver (未解决)


-在mac的终端面板输入uiautomatorviewer启动工具出现无法截图的问题
（暂未解决，需要重新对uiautomatorviewer进行打包，遇到mvn not found的问题）

"""
