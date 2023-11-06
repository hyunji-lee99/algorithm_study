import sys

n,m=map(int, sys.stdin.readline().split(' '))
nlist=list(map(int, sys.stdin.readline().split(' ')))
nlist.sort()

visited=[0]*n
arr=[0]*m
def dfs(cnt,num):
    if cnt==m:
        print(*arr, sep=' ')
        return

    for i in range(num+1, n):
        if visited[i]==0:
            arr[cnt]=nlist[i]
            visited[i]=1
            dfs(cnt+1, i)
            visited[i]=0

dfs(0,-1)
