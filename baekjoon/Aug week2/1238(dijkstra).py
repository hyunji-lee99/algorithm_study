import sys
import heapq


n,m,x=map(int, sys.stdin.readline().split(' '))
path=[[] for _ in range(n+1)]
# 역방향그래프
pathR=[[] for _ in range(n+1)]
for _ in range(m):
    s,e,t=map(int, sys.stdin.readline().split(' '))
    path[s].append((e,t))
    pathR[e].append((s,t))

# party에서 각 마을로 돌아가는 최단 경로
fromParty=[1e9]*(n+1)
fromParty[x]=0

heap=[]
heapq.heappush(heap, (0,x))
while heap:
    time, cur = heapq.heappop(heap)
    # 이미 처리되어 있는 지점이라면 즉, 이전에 계산된 최단 경로가 현재 이 time 값보다 작아서 현재 time을 가지고 더 이상 계산해 줄 필요가 없음
    if time > fromParty[cur]:
        continue
    for nn,nt in path[cur]:
        if fromParty[nn]>time+nt:
            fromParty[nn]=time+nt
            heapq.heappush(heap, (time+nt, nn))

# 각 마을에서 party로 가는 최단 경로
toParty=[1e9]*(n+1)
toParty[x]=0
heapR=[]
heapq.heappush(heapR, (0,x))
while heapR:
    time, cur = heapq.heappop(heapR)
    # 이미 처리되어 있는 지점이라면 즉, 이전에 계산된 최단 경로가 현재 이 time 값보다 작아서 현재 time을 가지고 더 이상 계산해 줄 필요가 없음
    if time > toParty[cur]:
        continue
    for nn,nt in pathR[cur]:
        if toParty[nn]>time+nt:
            toParty[nn]=time+nt
            heapq.heappush(heapR, (time+nt, nn))

ans=-1e9
for i in range(1,n+1):
    ans=max(ans, toParty[i]+fromParty[i])

print(ans)
