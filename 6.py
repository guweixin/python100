# -*- coding: utf-8 -*-
'''
题目：斐波那契数列。
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
在数学上，费波那契数列是以递归的方法来定义：
F0 = 0     (n=0)
F1 = 1    (n=1)
Fn = F[n-1]+ F[n-2](n=>2)
程序源代码：
'''
def fun(n):
    f=[0,1]
    if n<2:
        return f[n]
    for i in range(2,n+1):
        x = f[i-2] + f[i-1]
        f.append(x)
    return f[n]

print fun(10)