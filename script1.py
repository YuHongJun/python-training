#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# A first Python script

# import sys  # Load a library module
#
# print(sys.platform)
# print(2 ** 100)  # Raise 2 to a power
# x = 'Spam!'
# print(x * 8)  # String repetition

# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
# s1 = 72
# s2 = 85
# r = (85 - 72) / 72 * 100
# print('小明成绩提升百分点%.1f%%' % r)
#
# #小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# h = input('please input an height: ')
# height = float(h)
# w = input('please input an weight: ')
# weight = float(w)
# bmi = weight / (height ** 2)
# print('你的身高是%.2f m,体重是%.1f kg,BMI指数是%f ' %(height,weight,bmi))
#
# if bmi < 18.5:
#     print('过轻')
# elif 18.5 <= bmi < 25:
#     print('正常')
# elif 25 <= bmi < 28:
#     print('过重')
# elif 28 <= bmi < 32:
#     print('肥胖')
# else:
#     print('严重肥胖')

#range(101)就可以生成0-100的整数序列，计算如下
# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum)

#第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现：
# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n - 2
# print(sum)

# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
#
# ax2 + bx + c = 0
#
# 的两个解。
#
# 提示：计算平方根可以调用math.sqrt()函数

# import math
# def quadratic(a, b, c):
#     if b**2-4*a*c   ==0:
#         return -b/(2*a)
#     elif (b**2-4*a*c)   <0:
#         return '无解'
#     else:
#         n1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
#         n2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
#         return n1,n2
# print(quadratic(2, 3, 1))
# print(quadratic(1, 4, 4))

# 参数组合
#
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
#
# 比如定义一个函数，包含上述若干种参数：

# def f1(a, b, c=0, *args, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
#
# def f2(a, b, c=0, *, d, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
#
# args = (1, 2, 3)
# kw = {'d': 99, 'x': '#'}
# f1(args, kw)
# f1(*args, kw)
# f1(*args, *kw)
# f1(*args, **kw)

# f2(*args, **kw)

# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)
#
# print(fact(5))

# s=0
# def hanoi(n,a,b,c):
#     global s
#     if n==1:
#         s=s+1
#         print('第 %s 步：' % s)
#         print(a,'->',c)
#     else:
#         hanoi(n-1,a,c,b) #将前n-1个盘子从a移动到b上
#         hanoi(1, a, b, c) #将最底下的最后一个盘子从a移动到c上
#         hanoi(n - 1, b, a, c) #将b上的n-1个盘子移动到c上
#
#
# hanoi(3,'A','B','C')

#汉诺塔 http://baike.baidu.com/item/%E6%B1%89%E8%AF%BA%E5%A1%94/3468295

# B=[]
# def move(n,a,b,c):
#     if n==1:
#         buzhou=a+str(n)+'-->'+c+str(n)+'first'
#         B.append(buzhou)
#         return
#     else:
#         move(n-1,a,c,b)
#         buzhou = a + str(n) + '-->' + c + str(n)+'seco'
#         B.append(buzhou)
#         move(n-1,b,a,c)
# move(3,'A','B','C')
# print('共需操作'+str(len(B))+'次','操作过程为',B)
#共需操作7次 操作过程为
# ['A1-->C1first', 'A2-->B2seco', 'C1-->B1first', 'A3-->C3seco', 'B1-->A1first', 'B2-->C2seco', 'A1-->C1first']


L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)==True]
L3 = [s.lower() if isinstance(s,str) else s for s in L1]
L4 = [s.upper() if isinstance(s,str) is True else s for s in L1]
L5 = [s[:1].upper()+s[1:].lower() if isinstance(s,str) else s for s in L1]
print('L1:',L1)
print('L2:',L2)
print('L3:',L3)
print('L4:',L4)
print('L5:',L5)