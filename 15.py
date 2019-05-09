# -*- coding: utf-8 -*-
'''
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。
程序源代码：
'''
def fun(score):
    if(score<60):
        return "C"
    elif(score<90):
        return "B"
    else:
        return "A"

print fun(90)


# score = int(raw_input('输入分数:\n'))
# if score >= 90:
#     grade = 'A'
# elif score >= 60:
#     grade = 'B'
# else:
#     grade = 'C'
 
# print '%d 属于 %s' % (score,grade)