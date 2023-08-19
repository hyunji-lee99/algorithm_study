import sys
from collections import deque

n=int(sys.stdin.readline())

def bfs():
    global w
    global h
    directions=[(0,1),(0,-1),(1,0),(-1,0)]
    cnt = 0
    while queue:
        cnt+=1
        # 불의 상태를 먼저 update (상근이는 불이 옮겨진 칸 또는 붙으려는 칸으로 이동할 수 없음)
        while fire and fire[0][2] < cnt:
            y, x, time = fire.popleft()
            for di in directions:
                dy = y + di[1]
                dx = x + di[0]
                if 0 <= dy < h and 0 <= dx < w and (area[dy][dx] == '.' or area[dy][dx] == '@'):
                    fire.append((dy, dx, time + 1))
                    # dy, dx가 아니라 y,x를 넣어서 틀리고 있었음
                    area[dy][dx] = '*'

        while queue and queue[0][2] < cnt:
            y, x, time = queue.popleft()
            for di in directions:
                dy = y + di[1]
                dx = x + di[0]
                # 바깥으로 탈출한 경우
                if dy >= h or dy < 0 or dx >= w or dx < 0:
                    print(time + 1)
                    return
                else:
                    if visited[dy][dx] == 0 and area[dy][dx] == '.':
                        queue.append((dy, dx,time+1))
                        visited[dy][dx] = 1
    else:
        print('IMPOSSIBLE')


for i in range(n):
    queue = deque()
    fire=deque()
    w,h=map(int, sys.stdin.readline().split(' '))
    visited = [[0] * (w) for _ in range(h)]
    area=[]
    for j in range(h):
        tmp=list(sys.stdin.readline().strip())
        area.append(tmp)
    # 시작 위치 찾기
    for k in range(h):
        for l in range(w):
            if area[k][l]=='@':
                queue.append((k,l,0))
                visited[k][l]=1
            elif area[k][l]=='*':
                fire.append((k,l,0))

    bfs()


