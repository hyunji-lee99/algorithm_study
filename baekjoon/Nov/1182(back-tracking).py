import sys

n,s=map(int, sys.stdin.readline().split(' '))
nlist=list(map(int, sys.stdin.readline().split(' ')))
ans=0
visited=[0]*n
def dfs(cnt,num):
    global ans
    if cnt==m:
        if sum(arr)==s:
            ans+=1
        return

    for i in range(num+1,n):
        if visited[i]==0:
            visited[i]=1
            arr[cnt]=nlist[i]
            dfs(cnt+1,i)
            visited[i]=0

for m in range(1,n+1):
    arr = [0] * m
    dfs(0,-1)

print(ans)
