import sys

n,m=map(int, sys.stdin.readline().split(' '))

nlist=list(map(int, sys.stdin.readline().split(' ')))

visited=[0]*n
arr=[0]*m
ans=set()
def dfs(cnt):
    if cnt==m:
        ans.add(' '.join(map(str,arr)))
        return
    for i in range(n):
        if visited[i]==0:
            visited[i]=1
            arr[cnt]=nlist[i]
            dfs(cnt+1)
            visited[i]=0

dfs(0)

for s in sorted(ans,key=lambda x:list(map(int,x.split(' ')))):
    print(s)
