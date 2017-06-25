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
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

#第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现：
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)