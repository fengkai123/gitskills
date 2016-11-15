#codingutf-8
#创建一个类
class person:
    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print "hello,world! I am %s" % self.name


foo = person()
bar = person()
foo.setName("luke skywalker")
bar.setName("anakin skywalker")
foo.greet()
bar.greet()