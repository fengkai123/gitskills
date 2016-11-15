#coding=utf-8
from time import *
from random import *
date1 = (2008,1,1,0,0,0,-1,-1,-1)
date2 = (2009,1,1,0,0,0,-1,-1,-1)
time1 = mktime(date1)
time2 = mktime(date2)
random_time = uniform(time1,time2)
print asctime(localtime(random_time))