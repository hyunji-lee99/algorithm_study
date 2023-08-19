import sys
from collections import deque

n,q=map(int, sys.stdin.readline().split(' '))
# s,e,r : 동영상 p,q가 usado r로 연결되어 있다.
# dummy
network=[[] for _ in range(n+1)]
for _ in range(n-1):
    s,e,r=map(int, sys.stdin.readline().split(' '))
    network[s].append((e,r))
    network[e].append((s,r))

for _ in range(q):
    # 동영상 v를 보고 있는 소들 기준으로 usado가 k 이상인 동영상의 개수
    k,v=map(int, sys.stdin.readline().split(' '))
    # 모든 노드까지의 usado 구하기

    # 시간 초과 코드
    # ans=0
    # for num in range(1,n+1):
    #     if num==v:
    #         continue
    #     # usado는 그 경로의 모든 연결들의 usado 중 최솟값으로 함.
    #     queue=deque()
    #     queue.append((v,1e9))
    #     visited=[0]*(n+1)
    #     visited[v]=1
    #     while queue:
    #         cur, cur_usado=queue.popleft()
    #         if cur==num and cur_usado>=k:
    #                 ans+=1
    #                 break
    #         for next_node, next_usado in network[cur]:
    #             if visited[next_node]==0:
    #                 queue.append((next_node, min(cur_usado,next_usado)))
    #                 visited[next_node]=1
    # print(ans)

    # 동영상 사이의 거리가 k보다 작으면 더 이상 탐색을 하지않아야 함. -> k보다 작은 거리가 나타나면 무조건 두 영상 사이의 거리는 k 이하가 되므로.
    ans=0
    queue=deque()
    visited=[0]*(n+1)
    visited[v]=1
    for num, us in network[v]:
        queue.append((num, us))
        visited[num]=1

    while queue:
        cur_node, cur_usado=queue.popleft()
        if cur_usado>=k:
            ans+=1
            for next_node, next_usado in network[cur_node]:
                if visited[next_node]==0:
                    queue.append((next_node, min(cur_usado, next_usado)))
                    visited[next_node]=1

    print(ans)

