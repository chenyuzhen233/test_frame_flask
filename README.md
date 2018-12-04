# test_frame_flask
接口测试框架flask版（只提供API/**python3**）

## 题外话
初心是完善上一个接口测试框架，希望能有一个更为实用、美观的接口测试框架。在动手之前参考了其他测试大佬做的接口测试框架，其中有使用nose、unittest作为单元测试框架的，也有直接重写unittest库（为了获取更多的测试信息，例如：请求方法、状态码等requests的相关信息）作为单元测试框架的，有使用flask、django作为web框架的，也有使用wxpython制作GUI界面。
我觉得大家做的都很不错，其中依赖和定时任务的功能更是让我十分羡慕。如何才能在一个完善的接口测试框架中加入关联和依赖功能呢？如何在框架中加入定时任务功能呢？带着这两个问题，我在记事本上写下了项目的雏形。

## 项目介绍

### 框架环境
**开发语言**：python3.7
**主要库**：unittest、flask、flask_sqlalchemy
**数据库**：mysql

### 主要功能
- 创建、修改、删除、查询用例
- 根据测试用例的依赖属性，存储或者读取依赖关系
- 定时执行任务
- 输出测试报告
- 邮件发送测试报告
