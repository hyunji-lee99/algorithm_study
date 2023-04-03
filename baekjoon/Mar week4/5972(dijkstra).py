# 다익스트라 알고리즘 - dp방식으로 최단경로 구하기(heapq 우선순위큐 이용)
import sys
import heapq
from collections import deque

n,m=map(int, sys.stdin.readline().split(' '))
# dummy
graph=[[] for _ in range(n+1)]

for i in range(m):
    a,b,c=map(int, sys.stdin.readline().split(' '))
    graph[a].append((b,c))
    graph[b].append((a,c))

dp=[1e9]*(n+1)
def dijkstra():
    global dp, graph, n
    heap=[]
    # (cost, node)
    # cost순으로 오름차순 정렬
    heapq.heappush(heap, (0,1))
    # 1번 노드에서 시작
    dp[1]=0
    while heap:
        # 현재까지 계산한 1에서 출발해서 cur_node까지 오는 데에 걸리는 최단 비용 cur_cost
        cur_cost, cur_node = heapq.heappop(heap)
        for next_node, next_cost in graph[cur_node]:
            if dp[next_node]>next_cost+cur_cost:
                dp[next_node]=next_cost+cur_cost
                heapq.heappush(heap, (next_cost+cur_cost, next_node))

dijkstra()

print(dp[n])



