# -*- coding: utf-8 -*-
'''
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。
'''

#import string
s = raw_input('请输入字符串:\n')
letters=0
space=0
digit=0
other=0
for c in s:
    if c.isalpha():
        letters+=1
    elif c.isspace():
        space+=1
    elif c.isdigit:
        digit+=1
    else:
        other+=1
print "英文字母:%d、空格:%d、数字:%d、其它字符:%d" % (letters,space,digit,other)