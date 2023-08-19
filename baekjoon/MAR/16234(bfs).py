# 연합국이 한 개도 없을 때까지 반복해서 인구이동에 걸리는 날짜를 계산

import sys
from collections import deque

n,l,r=map(int, sys.stdin.readline().split(' '))
population=[]
for i in range(n):
    tmp=list(map(int, sys.stdin.readline().strip().split(' ')))
    population.append(tmp)

def bfs(i,j):
    global check
    union = []
    union.append((i,j,population[i][j]))
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        y, x = queue.popleft()
        for di in directions:
            dy = y + di[1]
            dx = x + di[0]
            if 0 <= dy < n and 0 <= dx < n and visited[dy][dx] == 0 and l <= abs(
                    population[y][x] - population[dy][dx]) <= r:
                queue.append((dy, dx))
                visited[dy][dx] = 1
                union.append((dy, dx, population[dy][dx]))

    if len(union)>1:
        check=1
        pvalue = [x[2] for x in union]
        psum = sum(pvalue) // len(union)
        for u in union:
            y, x, p = u
            population[y][x] = psum


day=0
check=1
while check==1:
    visited = [[0] * (n) for _ in range(n)]
    # bfsf로 돌았을 때 새로운 연합이 발생하는지 확인
    check = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0:
                bfs(i, j)
    if check == 1:
        day += 1

print(day)

