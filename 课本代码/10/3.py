#coding=utf-8
from random import randrange
num = input("how many dice:")#选择几个骰子
sides = input("how many sides per die?")#选择每个骰子的面数
sum = 0
for i in range(num):
    sum += (randrange(1,sides,1) + 1)
print "the result is ",sum