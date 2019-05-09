# -*- coding: utf-8 -*-
"""
Created on Sun May  5 17:56:36 2019

@author: em
"""
'''
题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
程序源代码：
'''

year = int(raw_input('year:\n'))
month = int(raw_input('month:\n'))
day = int(raw_input('day:\n'))
days=0
months=(0,31,28,31,30,31,30,31,31,30,31,30,31)
for i in range(0,month):
    days += months[i] 

days+=day

if month>2 and (year%100==0 or year%4==0 and year%100!=0):
    days+=1

print 'it is the %dth day.' %days