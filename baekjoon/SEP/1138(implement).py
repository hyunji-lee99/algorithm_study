import sys

n=int(sys.stdin.readline())
ans=[0]*(n)
height=list(map(int, sys.stdin.readline().strip().split(' ')))
ans[height[0]]=1
for i in range(1,n):
    count = 0
    for j in range(n):
        if ans[j]==0 and height[i] == count:
            ans[j] = i + 1
            break
        if ans[j]==0:
            count+=1

print(*ans, sep=' ')

