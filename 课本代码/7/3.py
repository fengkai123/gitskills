#coding=utf-8
#将其他类名写在class语句的括号内，可以定义超类
class Filter:
    def init(self):
        self.blocked = []
    def filter(self,squence):
        return [x for x in squence if x not in self.blocked]

class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']



f = Filter()
f.init()
print f.filter([1,2,3])

s = SPAMFilter()
s.init()
print s.blocked , f.blocked
print s.filter(['SPAM','eggs','SPAM','SPAM','bacon'])

print issubclass(SPAMFilter,Filter)
print issubclass(Filter,SPAMFilter)
print SPAMFilter.__bases__
print isinstance(s,SPAMFilter)
print isinstance(s,Filter)