# -*- coding: utf-8 -*-
'''
[扩展] 更多python-time教程，可访问http://www.liujiangblog.com/course/python/68
'''
'''
题目：暂停一秒输出，并格式化当前时间。
程序分析：无。
程序源代码：
'''
import time
 
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# print time.localtime(time.time())
# print time.strftime('%Y-%m-%d %H:%M:%S')
 # 暂停一秒
time.sleep(1)
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))