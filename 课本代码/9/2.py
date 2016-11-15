#coding=utf-8
class Brid:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print "Ahhhh..."
            self.hungry = False
        else:
            print "No thanks"


class SingBrid(Brid):
    def __init__(self):
        Brid.__init__(self)#绑定方法
        self.sound = "squawk"
    def sing(self):
        print self.sound

b = Brid()
b.eat()
b.eat()
print
sb = SingBrid()
sb.sing()
sb.eat()
sb.eat()