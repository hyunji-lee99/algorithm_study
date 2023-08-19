import sys
from collections import deque

# 도시의 수
n=int(sys.stdin.readline())
# 여행계획에 속한 도시의 수
m=int(sys.stdin.readline())
# 연결정보(dummy 포함)
graph=[[0]*(n+1)]+[[0]+list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]
# 여행 계획
plan=list(map(int, sys.stdin.readline().split(' ')))

def possible_bfs(dep, arv):
    global graph, n
    queue=deque()
    queue.append(dep)
    visited=[0]*(n+1)
    while queue:
        cur=queue.popleft()
        if cur==arv:
            return True
        visited[cur] = 1
        for i in range(1, n+1):
            if graph[cur][i]==1 and visited[i]==0:
                queue.append(i)

    return False




for idx in range(len(plan)-1):
    dep=plan[idx]
    arv=plan[idx+1]
    if possible_bfs(dep, arv):
        continue
    else:
        print('NO')
        sys.exit(0)

print('YES')


