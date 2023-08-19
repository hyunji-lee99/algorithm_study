import sys

v,e=map(int, sys.stdin.readline().split(' '))

dist=[[1e9]*(v+1) for _ in range(v+1)]
graph=[[] for _ in range(v+1)]

for _ in range(e):
    a,b,c=map(int, sys.stdin.readline().split(' '))
    dist[a][b]=c

# 1~v까지 경유한다고 가정하고, i부터 j까지 가는 길에 k번 노드를 경유했다가 가는 것이 더 빠른지 확인
for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1,v+1):
            dist[i][j]=min(dist[i][j], dist[i][k]+dist[k][j])

ans=1e9
for i in range(1, v+1):
    ans=min(ans, dist[i][i])

if ans==1e9:
    print(-1)
else:
    print(ans)

