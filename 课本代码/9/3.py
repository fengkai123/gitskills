#coding=utf-8
__metaclass__ = type    #注意super函数只能在新式类中起作用
class Brid:
    def __init__(self):
        self.hungry = True;
    def eat(self):
        if self.hungry:
            print "Ahh.."
            self.hungry = False
        else:
            print "NO thanks"

class SingBrid(Brid):
    def __init__(self):
        super(SingBrid,self).__init__()#使用super函数解决构造方法重写的问题
        self.sound = "Squawk"
    def sing(self):
        print self.sound

sb = SingBrid()
sb.sing()
sb.eat()