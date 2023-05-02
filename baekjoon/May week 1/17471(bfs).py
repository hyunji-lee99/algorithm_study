import sys
from itertools import combinations
from collections import deque

n=int(sys.stdin.readline())
# dummy
population=[0]+list(map(int, sys.stdin.readline().split(' ')))
graph=[[] for _ in range(n+1)]
for i in range(1, n+1):
    g=list(map(int, sys.stdin.readline().split(' ')))
    for j in range(1,g[0]+1):
        graph[i].append(g[j])

city=[x for x in range(1, n+1)]

def isConnected_bfs(team):
    global graph
    queue=deque()
    visited=[0]*(n+1)
    queue.append(team[0])
    visited[team[0]]=1
    while queue:
        cur=queue.popleft()
        for node in graph[cur]:
            if visited[node]==0 and (node in team):
                queue.append(node)
                visited[node]=1
    # queue 종료 후 team에 해당하는 모든 노드를 방문한 경우
    for t in team:
        if visited[t]==0:
            return False
    return True


minvalue=1e9
for p in range(1,n//2+1):
    red=list(combinations(city, p))
    # 구역을 나눌 수 있는 모든 경우의 수
    for r in red:
        rlist=list(r)
        blue=[x for x in city if x not in rlist]
        # red팀과 blue팀이 모두 각자 연결되어 있는 경우인지
        if isConnected_bfs(rlist) and isConnected_bfs(blue):
            red_popul=0
            blue_popul=0
            for i in range(1, n+1):
                if i in rlist:
                    red_popul+=population[i]
                else:
                    blue_popul+=population[i]
            diff_pop=abs(red_popul-blue_popul)
            minvalue=min(diff_pop, minvalue)

# 두 선거구로 나눌 수 있는 방법이 없는 경우
if minvalue==1e9:
    print(-1)
else:
    print(minvalue)


