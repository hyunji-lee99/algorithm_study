import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split(' '))
jido=[]
for i in range(n):
    tmp=list(map(int,list(sys.stdin.readline().strip())))
    jido.append(tmp)

di=[(0,1),(0,-1),(1,0),(-1,0)]
queue=deque()
visited=[]
queue.append((0,0,1))
visited.append((0,0))
while queue:
    y,x,distance=queue.popleft()
    if y==n-1 and x==m-1:
        print(distance)
        sys.exit(0)
    for d in di:
        dx=x+d[0]
        dy=y+d[1]
        if 0<=dx<m and 0<=dy<n and jido[dy][dx]==1 and (dy,dx) not in visited:
            visited.append((dy,dx))
            queue.append((dy,dx,distance+1))


