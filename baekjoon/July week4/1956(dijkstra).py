import sys
import heapq

v,e=map(int, sys.stdin.readline().split(' '))
# 최소 거리 저장할 배열
dist=[[1e9]*(v+1) for _ in range(v+1)]
heap=[]
graph=[[] for _ in range(v+1)]

for _ in range(e):
    a,b,c=map(int, sys.stdin.readline().split(' '))
    graph[a].append((b,c))
    dist[a][b]=c
    heapq.heappush(heap, (c,a,b))

while heap:
    # 거리, 출발지, 목적지
    d, a, b=heapq.heappop(heap)
    # 출발지와 목적지가 같으면 사이클 찾은 것. heap에 넣어뒀기 때문에 사이클 발견하자마자 경로 길이 출력하고 break 해주면 됨
    if a==b:
        print(d)
        break
    for node, w in graph[b]:
        # a->node로 가는 길에 b를 들렸다 가는 것이 더 빠른지
        new_dist=w+d
        if new_dist<dist[a][node]:
            dist[a][node]=new_dist
            heapq.heappush(heap, (new_dist, a, node))
else:
    # heap이 모두 소진될 때까지 break에 걸리지 않으면 사이클이 존재하지 않는 것이므로 -1
    print(-1)
