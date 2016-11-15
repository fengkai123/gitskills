#coding=utf-8
#创建一个私有类
class Secretive:
    def __inaccessible(self):    #方法前面加双下划线，可以使其变为私有的，即从外部无法访问
        print "bet you can't see me!"

    def accessible(self):
        print "the secet message is:"
        self.__inaccessible()


s = Secretive()
s.accessible()
