import sys

n,m=map(int, sys.stdin.readline().split(' '))
nlist=list(map(int, sys.stdin.readline().split(' ')))
nlist.sort()

arr=[0]*m
def dfs(cnt):
    if cnt==m:
        print(*arr, sep=' ')
        return

    for i in range(n):
        arr[cnt]=nlist[i]
        dfs(cnt+1)

dfs(0)
