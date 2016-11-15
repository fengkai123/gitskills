#coding:utf-8
try:
    x = float(input("enter a number:"))
    y = input("enter the two number:")
    print x/y
except (ZeroDivisionError,TypeError):
    print "y be a number!"
else:   #错误没有发生时，执行一段说明代码是很有用的
    print "Ah ... It went as planned."