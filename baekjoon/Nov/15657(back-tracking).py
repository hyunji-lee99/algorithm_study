import sys

n,m=map(int, sys.stdin.readline().split(' '))
nlist=list(map(int, sys.stdin.readline().split(' ')))
nlist.sort()
arr=[0]*m
def dfs(cnt, num):
    if cnt==m:
        print(*arr, sep=' ')
        return
    for i in range(num, n):
        arr[cnt]=nlist[i]
        dfs(cnt+1, i)

dfs(0,0)
