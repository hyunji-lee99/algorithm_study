# n : 수의 개수
# a1,...,an : 수열
# 차례대로 덧셈의 개수, 뺄셈의 개수, 곱셈의 개수, 나눗셈의 개수로 주어짐

import sys

n=int(sys.stdin.readline())
an=list(map(int, sys.stdin.readline().strip().split(' ')))
operator=list(map(int, sys.stdin.readline().strip().split(' ')))

max=-1e9
min=1e9
def dfs(index, num):
    global min, max,n
    if index==n:
        if max<num:
            max=num
        if min>num:
            min=num

    for i in range(4):
        if operator[i]>0:
            if i==0:
                operator[i]-=1
                dfs(index+1, num+an[index])
                operator[i]+=1
            elif i==1:
                operator[i]-=1
                dfs(index+1, num-an[index])
                operator[i]+=1
            elif i==2:
                operator[i]-=1
                dfs(index+1, num*an[index])
                operator[i]+=1
            elif i==3:
                operator[i]-=1
                dfs(index+1, int(num/an[index]))
                operator[i]+=1

dfs(1,an[0])
print(max)
print(min)