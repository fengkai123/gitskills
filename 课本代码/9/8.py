#coding=utf-8

#从迭代器得到序列
class TestIterator:
    value = 0
    def next(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value
    def __iter__(self):
        return self

t = TestIterator()
print list(t)