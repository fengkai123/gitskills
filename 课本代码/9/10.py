#coding=utf-8
#八皇后问题
def conflict(state,nextx):
    nexty = len(state)
    for i in range(nexty):
        if abs(state[i]-nextx) in (0,nexty - i):
            return True
    return False
"""
def queens(num,state):
    if len(state) == num -1:
        for pos in range(num):
            if not conflict(state,pos):
                 yield pos
    else:
        for pos in range(num):
            if not conflict(state,pos):
                for result in queens(num,state + (pos,)):
                    yield (pos,) + result
"""
def queens(num=8,state=()):
    for pos in range(num):
        if not conflict(state,pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for reslut in queens(num,state + (pos,)):
                    yield (pos,) + reslut

print list(queens(3))
print list(queens(4))
for solution in queens(8):
    print solution
print len(list(queens(8)))

def prettyprint(solution):
    def line(pos,length = len(solution)):
        return '.' * (pos) + 'X' + '.' * (length - pos -1)
    for pos in solution:
        print line(pos)

import random
prettyprint(random.choice(list(queens(8))))