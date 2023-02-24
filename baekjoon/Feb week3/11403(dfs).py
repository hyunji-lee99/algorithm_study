# 가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서, i에서 j로 가는 경로가 있는지 없는지 구하는 프로그램을 작성하시오.
# n : 노드의 개수
# n*n 인접행렬로 주어짐

import sys

n=int(sys.stdin.readline().strip())
adjacent=[]
graph=[[] for _ in range(n)]
for i in range(n):
    tmp=sys.stdin.readline().strip().split(' ')
    adjacent.append(tmp)
    for j in range(n):
        if tmp[j]=='1':
            graph[i].append(j)

#각 경로가 연결되어 있는지 확인하는 dfs
check=0

#재귀 dfs는 return으로 결과를 확인하지말고, 어떤 체크값을 줘서 설정해야 잘 돌아감
def dfs(i,j,visited):
    global check
    for node in graph[i]:
        if node==j:
            check=1
            return
        if visited[node]==0:
            visited[node] = 1
            dfs(node, j,visited)


for i in range(n):
    for j in range(n):
        visited = [0] * n
        check=0
        dfs(i,j,visited)
        if check==1:
            adjacent[i][j]='1'

for i in range(n):
    for j in range(n):
        print(adjacent[i][j], end=' ')
    print('')
