# 4%에서 틀림 원인 찾는 중

import sys
from collections import deque

n,m,x=map(int, sys.stdin.readline().split(' '))
graph=[[] for _ in range(n+1)]
for _ in range(m):
    s,e,t=map(int, sys.stdin.readline().split(' '))
    graph[s].append((e,t))

# x번 마을에 모임
# 각 마을에서부터 x번에 갔다가 다시 자신의 마을로 돌아오는 최단 거리 구해서 그 중 최댓값 구하기
# 다익스트라
def cal_st(num):
    global x
    # num에서 x까지 가는 최단 경로
    go_dijkstra=[1e9]*(n+1)
    go_visited=[0]*(n+1)
    go_dijkstra[num]=0
    go_queue=deque()
    go_queue.append(num)
    while go_queue:
        cur=go_queue.popleft()
        go_visited[cur]=1
        for node, time in graph[cur]:
            if go_visited[node]==0:
                go_dijkstra[node]=min(go_dijkstra[node], go_dijkstra[cur]+time)
                go_queue.append(node)

    # x에서 num까지 가는 최단 경로
    back_dijkstra=[1e9]*(n+1)
    back_visited=[0]*(n+1)
    back_dijkstra[x]=0
    back_queue=deque()
    back_queue.append(x)
    while back_queue:
        cur=back_queue.popleft()
        back_visited[cur]=1
        for node, time in graph[cur]:
            if back_visited[node]==0:
                back_dijkstra[node]=min(back_dijkstra[node], back_dijkstra[cur]+time)
                back_queue.append(node)

    return go_dijkstra[x]+back_dijkstra[num]

# max값 구하기
ans=-1e9
for i in range(1,n+1):
    ans=max(ans, cal_st(i))

print(ans)

