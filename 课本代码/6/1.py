#coding=utf-8

def fibs(num):
  result = [0,1]
  for i in range(num-2):
     result.append(result[-1] + result[-2])
  return result

print fibs(10)

def factorial(n):
    if n==1:
        return 1
    else:
        return factorial(n-1)*n

print factorial(16)