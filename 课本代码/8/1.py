#coding:utf-8
#捕捉异常可以使用try/except来实现
try:
    x = float(input("enter a number:"))
    y = input("enter the two number:")
    print x / y
except ZeroDivisionError:
    print "the two number can't be zero!"