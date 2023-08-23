import sys
from collections import deque

w,h=map(int, sys.stdin.readline().split(' '))
area=[list(sys.stdin.readline().strip()) for _ in range(h)]

C=[]
for i in range(h):
    for j in range(w):
        if area[i][j]=='C':
            C.append((i,j))
# 방향과 위치에 따른 최소 거울의 개수를 저장하는 visited 배열
visited=[[[1e9]*4 for _ in range(w)] for _ in range(h)]
queue=deque()
# 현재 위치, 현재 방향, 거울 개수
queue.append((C[0][0],C[0][1],0,0))
visited[C[0][0]][C[0][1]][0]=0
queue.append((C[0][0],C[0][1],1,0))
visited[C[0][0]][C[0][1]][1]=0
queue.append((C[0][0],C[0][1],2,0))
visited[C[0][0]][C[0][1]][2]=0
queue.append((C[0][0],C[0][1],3,0))
visited[C[0][0]][C[0][1]][3]=0

directions=[(0,1),(1,0),(-1,0),(0,-1)]
while queue:
    y,x,d,m=queue.popleft()
    for i in range(4):
        dy=y+directions[i][0]
        dx=x+directions[i][1]
        if 0<=dy<h and 0<=dx<w and area[dy][dx]!='*':
            # 현재 방향과 다르다면
            if i!=d and m+1<visited[dy][dx][i]:
                visited[dy][dx][i]=m+1
                queue.append((dy,dx,i,m+1))
            elif i==d and m<visited[dy][dx][i]:
                visited[dy][dx][i]=m
                queue.append((dy,dx,i,m))

print(min(visited[C[1][0]][C[1][1]]))


