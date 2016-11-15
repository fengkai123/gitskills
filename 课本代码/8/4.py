#coding:utf-8
while True:
    try:
      x = float(input("enter a number:"))
      y = input("enter the two number:")
      print x/y
    except:
       print "Invalid input! please try again..."
    else:   #实现循环
       break