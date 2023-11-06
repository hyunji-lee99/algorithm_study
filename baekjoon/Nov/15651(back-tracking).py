import sys

n,m=map(int, sys.stdin.readline().split(' '))

arr=[0]*m
def dfs(cnt):
    if cnt==m:
        print(*arr,sep=' ')
        return
    for i in range(1,n+1):
        arr[cnt]=i
        dfs(cnt+1)

dfs(0)
