import sys
input=sys.stdin.readline
n,m=map(int, input().split(' '))
nlist=list(map(int, input().split(' ')))
nlist.sort()

visited=[0]*n
arr=[0]*m
ans=set()
def dfs(cnt, num):
    if cnt==m:
        ans.add(' '.join(map(str, arr)))
        return

    for i in range(num+1,n):
        if visited[i]==0:
            visited[i]=1
            arr[cnt]=nlist[i]
            dfs(cnt+1, i)
            visited[i]=0

dfs(0,-1)

for s in sorted(ans, key=lambda x:list(map(int, x.split(' ')))):
    print(s)
