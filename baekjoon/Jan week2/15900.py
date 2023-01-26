# 루트노드부터 리프노드까지의 거리를 depth라고 할 때 dfs를 통해서 구한 depth가 모두 짝수일 경우
# 선으로 시작하는 성원이는 형석이를 이길 수 없다. 그러나 dfs를 통해서 구한 depth들 중에서 홀수의
# 개수가 1개가 있다면 게임을 이길 수 있게되지만 홀수의 개수가 짝수인 경우라면 게임을 이길 수 없게 된다.

import sys
sys.setrecursionlimit(10**5)

n=int(sys.stdin.readline())
graph=[[] for _ in range(n)]
visited=[0  for _ in range(n)]
distance=[0 for _ in range(n)]

for i in range(n-1):
    x,y=map(int,sys.stdin.readline().split(' '))
    graph[x-1].append(y-1)
    graph[y-1].append(x-1)

#dfs 이용해서 각 리프노드의 깊이 구하기
def dfs(cur):
    visited[cur]=1
    for next in graph[cur]:
        #방문한 적없는 노드인 경우
        if visited[next]==0:
            #부모노드의 저장된 거리에 +1해서 저장
            distance[next]=distance[cur]+1
            #dfs로 다음 노드기준으로 dfs 시작
            dfs(next)

dfs(0)

answer=0

for i in range(1,n):
    #리프노드 판별(연결된 노드가 1개인 경우)
    if len(graph[i])==1:
        answer+=distance[i]

if answer%2==1:
    print('Yes')
else:
    print('No')
