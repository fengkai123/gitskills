#coding=utf-8
def process(string):
    print 'processing',string
import fileinput
for line in fileinput.input('C:\Users\Administrator\somefile.txt'):  #使用fileinput模块
    process(line)
"""
f = open('C:\Users\Administrator\somefile.txt')
"""
"""
char = f.read(1)#每次读取一个字符
while char:
    process(char)
    char = f.read(1)
f.close()
"""
"""
while True:
    line = f.readline()  #每次读取一行
    if not line:
        break
    process(line)
f.close()
"""
"""
for char in f.readlines():
    process(char)
f.close()
"""