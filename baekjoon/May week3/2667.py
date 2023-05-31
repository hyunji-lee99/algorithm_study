import sys
from collections import deque

n=int(sys.stdin.readline())
area=[list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
directions=[(0,1),(1,0),(0,-1),(-1,0)]
visited=[[0]*n for _ in range(n)]
#bfs를 사용해서 각각의 단지 크기를 구하고, 총 단지의 개수를 구하자
areas=[]
size = 0
for i in range(n):
    for j in range(n):
        if area[i][j]==1 and visited[i][j]==0:
            queue=deque()
            queue.append((i,j))
            tmp_size=0
            while queue:
                y,x=queue.popleft()
                for di in directions:
                    dy=y+di[0]
                    dx=x+di[1]
                    if 0<=dy<n and 0<=dx<n and visited[dy][dx]==0 and area[dy][dx]==1:
                        queue.append((dy,dx))
                        visited[dy][dx]=1
                        tmp_size += 1
            # 가구가 하나밖에 없을 때
            if tmp_size==0:
                areas.append(1)
            else:
                areas.append(tmp_size)
            size+=1


print(size)
areas.sort()
for a in areas:
    print(a)


