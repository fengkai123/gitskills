#coding=utf-8                                                #  1
import fileinput                                             #  2
for line in fileinput.input(inplace=True):                   #  3
    line = line.rstrip()                                     #  4
    num = fileinput.lineno()                                 #  5
    print '%-60s # %2i' % (line,num)                         #  6
