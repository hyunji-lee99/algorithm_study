import sys
from collections import deque

n=int(sys.stdin.readline())
icecream=[list(sys.stdin.readline().strip()) for _ in range(n)]
visited=[[0]*(n) for _ in range(n)]

def find_area_and_length():
    global visited, queue, icecream
    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    area=0
    length=0
    while queue:
        y,x=queue.popleft()
        # 면적 구하기
        area += 1
        # 길이 구하기 -> 상하좌우로 범위를 벗어나거나, '.'이 존재하는 경우 length+=1
        for di in directions:
            dy=y+di[0]
            dx=x+di[1]
            if 0<=dy<n and 0<=dx<n:
                if icecream[dy][dx]=='.':
                    length+=1
            else:
                length+=1
        for di in directions:
            dy=y+di[0]
            dx=x+di[1]
            if 0<=dy<n and 0<=dx<n and visited[dy][dx]==0 and icecream[dy][dx]=='#':
                queue.append((dy,dx))
                visited[dy][dx]=1
    return area, length

max_area=0
min_length=0
for i in range(n):
    for j in range(n):
        if icecream[i][j]=='#' and visited[i][j]==0:
            queue=deque()
            queue.append((i,j))
            visited[i][j]=1
            area, length=find_area_and_length()
            if area>max_area:
                max_area=area
                min_length=length
            elif area==max_area:
                min_length=min(length, min_length)

print(max_area, min_length)