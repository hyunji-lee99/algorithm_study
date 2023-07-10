import sys
from collections import deque

n,k,r=map(int, sys.stdin.readline().split(' '))

# dummy
graph=[[0]*(n+1) for _ in range(n+1)]
# 3차원 배열
ways=[[[] for _ in range(n+1)] for _ in range(n+1)]
for i in range(1,r+1):
    r,c,r_,c_=map(int, sys.stdin.readline().split(' '))
    ways[r][c].append((r_, c_))
    ways[r_][c_].append((r,c))

cow=[]
for _ in range(k):
    y,x=map(int, sys.stdin.readline().split(' '))
    cow.append((y,x))


def impossible_meet_cow(sy, sx, ey, ex):
    global ways
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue=deque()
    queue.append((sy,sx))
    visited=[[0]*(n+1) for _ in range(n+1)]
    visited[sy][sx]=1
    while queue:
        cury, curx=queue.popleft()
        if cury==ey and curx==ex:
            return False
        for di in directions:
            dy=cury+di[0]
            dx=curx+di[1]
            if 1<=dy<=n and 1<=dx<=n and visited[dy][dx]==0:
                # (dy,dx)가 ways[cury][curx]에 존재하는지 즉, 길을 건너야만 갈 수 있는 곳인지 확인
                if (dy,dx) not in ways[cury][curx]:
                    queue.append((dy,dx))
                    visited[dy][dx]=1
    else:
        return True

ans=0
for i in range(k):
    for j in range(i,k):
        # start cow
        sc_y, sc_x=cow[i]
        # end cow
        ec_y, ec_x=cow[j]
        if impossible_meet_cow(sc_y, sc_x, ec_y,ec_x):
            ans+=1

print(ans)
