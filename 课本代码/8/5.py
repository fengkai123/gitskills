#coding:utf-8
while True:
    try:
        x = float(input("enter the frist number:"))
        y = input("enter the second number:")
        print "x/y is:",x/y
    except Exception,e:
        print "Invalid input:",e
        print "please try again!"
    else:
        break