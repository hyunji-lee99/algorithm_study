import sys

n,m=map(int, sys.stdin.readline().split(' '))

def factorial(num):
    if num>1:
        return num*factorial(num-1)
    else:
        return 1

print(factorial(n)//(factorial(n-m)*factorial(m)))