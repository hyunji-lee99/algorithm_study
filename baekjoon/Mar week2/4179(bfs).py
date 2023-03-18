# 5427번 불 문제와 동일

import sys
from collections import deque

r,c=map(int, sys.stdin.readline().split(' '))
graph=[]
for i in range(r):
    tmp=list(sys.stdin.readline().strip())
    graph.append(tmp)


def bfs():
    cnt=0
    directions=[(0,1),(0,-1),(1,0),(-1,0)]
    while queue_jihun:
        cnt += 1
        # 불의 위치 업데이트
        while queue_fire and queue_fire[0][2] < cnt:
            y, x, time = queue_fire.popleft()
            for di in directions:
                dy = y + di[1]
                dx = x + di[0]
                if 0 <= dy < r and 0 <= dx < c and (graph[dy][dx] == '.' or graph[dy][dx] == 'J'):
                    queue_fire.append((dy, dx, time + 1))
                    graph[dy][dx] = 'F'
        # 지훈 이동
        while queue_jihun and queue_jihun[0][2] < cnt:
            y, x, time = queue_jihun.popleft()
            for di in directions:
                dy = y + di[1]
                dx = x + di[0]
                if dy<0 or dy>=r or dx<0 or dx>=c:
                    print(time+1)
                    return
                elif 0 <= dy < r and 0 <= dx < c and graph[dy][dx] == '.' and visited_jihun[dy][dx] == 0:
                    queue_jihun.append((dy, dx, time + 1))
                    visited_jihun[dy][dx] = 1
    else:
        print('IMPOSSIBLE')



queue_jihun=deque()
visited_jihun=[[0]*c for _ in range(r)]

queue_fire=deque()

for i in range(r):
    for j in range(c):
        if graph[i][j]=='J':
            queue_jihun.append((i,j,0))
            visited_jihun[i][j] = 1
        elif graph[i][j]=='F':
            queue_fire.append((i,j,0))

bfs()