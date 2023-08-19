import sys
from collections import deque

w,h=map(int, sys.stdin.readline().split(' '))
raser=[list(sys.stdin.readline().strip()) for _ in range(h)]

def bfs(start, end):
    global raser, w,h
    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    queue=deque()
    # init
    # 시작 위치에서 각각 방향으로 레이저 쏘는 경우 모두 queue에 넣어줌
    # 이후 탐색과정에서 방향이 바뀌는 경우에 mirror+1

    # 방문 여부 저장
    check = [[0] * w for _ in range(h)]
    check[start[0]][start[1]] = 1
    # 최소 방문횟수 저장
    visited = [[0] * w for _ in range(h)]

    for di in directions:
        dy=start[0]+di[0]
        dx=start[1]+di[1]
        if 0<=dy<h and 0<=dx<w and raser[dy][dx]!='*':
            queue.append((dy, dx, di, 0))
            check[dy][dx] = 1

    min_mirror=1e9
    while queue:
        cury, curx, dir, mirror=queue.popleft()
        if cury==end[0] and curx==end[1]:
            min_mirror=min(min_mirror, mirror)
            continue
        for di in directions:
            dy=cury+di[0]
            dx=curx+di[1]
            if 0<=dy<h and 0<=dx<w and raser[dy][dx]!='*':
                # 아예 방문한 적이 없다면
                if check[dy][dx]==0:
                    # 현재 방향과 동일한 방향이라면
                    if dir==di:
                        queue.append((dy,dx,dir,mirror))
                        visited[dy][dx]=mirror
                        check[dy][dx]=1
                    else:
                        queue.append((dy,dx,di,mirror+1))
                        visited[dy][dx]=mirror+1
                        check[dy][dx] = 1
                # 방문한 적은 있으나, mirror의 개수가 현재 위치에 저장된 mirror의 개수보다 작다면
                else:
                    if dir==di and visited[dy][dx]>=mirror:
                        visited[dy][dx]=mirror
                        queue.append((dy,dx,dir,mirror))
                    elif dir!=di and visited[dy][dx]>=mirror+1:
                        visited[dy][dx]=mirror+1
                        queue.append((dy,dx,di,mirror+1))
    return min_mirror

c=[]
for i in range(h):
    for j in range(w):
        if raser[i][j]=='C':
            c.append((i,j))

print(bfs(c[0],c[1]))
