import sys

n=int(sys.stdin.readline())
path=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]


ans=1e9
visited=[0]*n
def dfs(start, cnt, cusum, cur):
    global ans
    if cusum>0 and cnt==n-1:
        if path[cur][start]!=0:
            ans=min(cusum+path[cur][start], ans)
        return
    for i in range(n):
        if path[cur][i]!=0 and visited[i]==0:
            visited[i]=1
            dfs(start,cnt+1,cusum+path[cur][i], i)
            visited[i]=0

for i in range(n):
    visited[i]=1
    dfs(i,0,0,i)
    visited[i]=0

print(ans)