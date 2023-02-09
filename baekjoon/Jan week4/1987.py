import sys
from collections import deque
r,c=map(int, sys.stdin.readline().split(' '))
map=[]
for i in range(r):
    alpha=list(sys.stdin.readline().strip())
    map.append(alpha)

#init
step=1
di=[(0,1),(1,0),(-1,0),(0,-1)]
visited=[[0 for _ in range(c)] for _ in range(r)]
visited_alpha=[]
#bfs
queue=deque()
queue.append((0,0))

while queue:
    x,y=queue.popleft()
    visited[x][y]=1
    visited_alpha.append(map[x][y])
    for d in di:
        dx=x+d[0]
        dy=y+d[1]
        if 0<=dx<r and 0<=dy<c and visited[dx][dy] == 0 and map[dx][dy] not in visited_alpha:
            queue.append((dx,dy))
            step+=1
            #생각 더 해보자!

print(step)


