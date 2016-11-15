#coding=utf-8
#多个超类
class Calculator:
    def claculate(self,expression):
        self.value = eval(expression)

class Talker:
    def talk(self):
        print "Hi,my value is", self.value

class TalkingCalculator(Calculator,Talker):
    pass


tc = TalkingCalculator()
tc.claculate('1+2*3')
tc.talk()

