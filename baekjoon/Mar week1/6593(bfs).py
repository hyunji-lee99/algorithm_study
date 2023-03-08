# l, r, c : 상범 빌딩의 층 수,  상범빌딩의 한 층의 행과 열
# 각 줄이 c개의 문자열로 이루어진 r개의 행이 l번 주어진다.
# 금으로 막혀있어 지나갈 수 없는 칸은 '#'
# 비어있는 칸은 '.'
# 시작 지점은 'S'
# 3차원 bfs 문제인 듯!

import sys
from collections import deque

while True:
    l, r, c = map(int, sys.stdin.readline().strip().split(' '))
    if l==0 and r==0 and c==0:
        break
    #init
    building=[]
    floor=[]
    queue=deque()
    visited=[[[0]*(c) for _ in range(r)] for _ in range(l)]
    #동,서,남,북,상,하
    directions=[(0,1,0),(0,-1,0),(0,0,-1),(0,0,1),(1,0,0),(-1,0,0)]

    # 입력받기
    for i in range(l):
        for j in range(r):
            tmp = list(sys.stdin.readline().strip())
            floor.append(tmp)
        building.append(floor.copy())
        sys.stdin.readline()
        floor.clear()

    #시작위치 찾기
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if building[i][j][k]=='S':
                    queue.append((i,j,k,0))
                    visited[i][j][k]=1
                    break
    # bfs로 최단경로 찾기
    while queue:
        z,y,x,time=queue.popleft()
        if building[z][y][x]=='E':
            print('Escaped in '+str(time)+' minute(s).')
            break
        for di in directions:
            dz=z+di[0]
            dy=y+di[2]
            dx=x+di[1]
            if 0<=dz<l and 0<=dy<r and 0<=dx<c:
                if building[dz][dy][dx]!='#' and visited[dz][dy][dx]==0:
                    queue.append((dz,dy,dx,time+1))
                    visited[dz][dy][dx]=1

    else:
        print('Trapped!')

