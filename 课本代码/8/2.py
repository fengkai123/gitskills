#coding:utf-8
try:
    x = float(input("enter a number:"))
    y = input("enter the two number:")
    print x/y
except ZeroDivisionError:
    print "y can't be zero!"
except TypeError:
    print "y be a number!"