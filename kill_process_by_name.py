#!/usr/bin/env Python3
#coding:utf8
import os


# def log(func):
#     process_name = 'tomcat_sf'
#     def wrapper():
#         print(" 开始杀进程：%s"%process_name)
#         func()
#         print("%s已停止" % process_name)
#     return wrapper


# @log
def kill_process_by_name(process_name):
    cmd = "ps -ef|grep %s|grep -v grep"%process_name
    output = os.system(cmd)
    print(output)

kill_process_by_name('audit-center')