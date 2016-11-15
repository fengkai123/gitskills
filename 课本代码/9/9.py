#coding=utf-8
#任何包含yield语句的函数成为生成器
nested = [[1,2],[3,4],[5]]
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element


print list(flatten(nested))


#递归生成器
def flatten(nested):
    try:
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested

print list(flatten([[[1],2],3,4,[5,[6,7]],8]))


def flatten(nested):
    try:
        try:nested + ""
        except TypeError:pass
        else:raise TypeError
        for sublist in nested:
            for element in flatten(nested):
                yield element
    except TypeError:
        yield nested