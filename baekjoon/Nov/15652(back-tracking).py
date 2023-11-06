import sys

n,m=map(int, sys.stdin.readline().split(' '))

arr=[0]*m
def dfs(cnt, num):
    if cnt==m:
        print(*arr,sep=' ')
        return

    for i in range(num,n+1):
        arr[cnt]=i
        dfs(cnt+1, i)

dfs(0,1)