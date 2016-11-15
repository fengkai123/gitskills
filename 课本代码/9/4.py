#coding=utf-8
def checkIndex(key):
    """
    所给的键是能接受的索引吗？
    为了能够被接受，键应该是一个非负整数。如果它不是一个整数，会引发TypeError；如果他是个负数，会引发IndexError.
    """
    if not isinstance(key,(int,long)):
        raise TypeError
    if key<0:
        raise IndexError
class ArithmeticSequence:
    def __init__(self,start=0,step=1):
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        checkIndex(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key*self.step

    def __setitem__(self, key, value):
        checkIndex(key)
        self.changed[key] = value

s = ArithmeticSequence(1,2)
print s[4]
s[4] = 2
print s[4]
print s[5]