import sys
from collections import deque

n=int(sys.stdin.readline())

maxheight=-1e9
minheight=1e9
heights=[]
for _ in range(n):
    tmp=list(map(int, sys.stdin.readline().strip().split(' ')))
    maxheight=max(maxheight, max(tmp))
    minheight=min(minheight, min(tmp))
    heights.append(tmp)

def bfs_find_safezone(y,x,h):
    global heights, visited
    queue=deque()
    queue.append((y,x))
    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    while queue:
        cury, curx=queue.popleft()
        for di in directions:
            dy=cury+di[0]
            dx=curx+di[1]
            if 0<=dy<n and 0<=dx<n and visited[dy][dx]==0 and heights[dy][dx]>h:
                queue.append((dy,dx))
                visited[dy][dx]=1

ans=0
for h in range(minheight-1, maxheight):
    visited=[[0]*n for _ in range(n)]
    safezone_number=0
    for i in range(n):
        for j in range(n):
            # h보다 더 높은 건물은 물에 잠기지 않는다.
            if heights[i][j]>h and visited[i][j]==0:
                visited[i][j]=1
                bfs_find_safezone(i,j,h)
                safezone_number+=1
    ans=max(ans, safezone_number)


print(ans)




