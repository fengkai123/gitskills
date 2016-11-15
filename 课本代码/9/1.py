#coding=utf-8
class FooBar:
    def __init__(self,value=42):
        self.value = value

f = FooBar()
print f.value

f= FooBar("this is a contructor argument")
print f.value