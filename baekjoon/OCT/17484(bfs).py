import sys
from collections import deque

n,m=map(int, sys.stdin.readline().split(' '))
fuel=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]

queue=deque()
# 첫 번째 행 좌표 모두 넣기
for i in range(m):
    # 현재 좌표, 축적 연료, 이전 방향(첫 시작이므로 방향 정보 없음 -1로 통일)
    queue.append([0,i,fuel[0][i],-1])

ans=1e9
directions=[(1,-1),(1,0),(1,1)]
while queue:
    y, x, f, d=queue.popleft()
    if y==n-1:
        ans=min(ans, f)
        continue

    for i in range(3):
        dy=y+directions[i][0]
        dx=x+directions[i][1]
        if 0<=dy<n and 0<=dx<m and d!=i:
            queue.append([dy,dx,f+fuel[dy][dx],i])

print(ans)

