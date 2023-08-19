# 3차원 배열 bfs
import sys
from collections import deque

m,n,h=map(int, sys.stdin.readline().split(' '))

# 3차원 배열로 현재 토마토 창고 상태 저장하자
storage=[[list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)] for _ in range(h)]
# storage[i][j][k] -> i번째 층 j행 k열

notripen=0
ripen=deque()
visited=[[[0]*m for _ in range(n)] for _ in range(h)]
for i in range(h):
    for j in range(n):
        for k in range(m):
            # 익은 토마토의 정보
            if storage[i][j][k]==1:
                visited[i][j][k] = 1
                ripen.append((i,j,k))
            # 익지 않은 토마토의 개수
            elif storage[i][j][k]==0:
                notripen+=1

def spread_ripen():
    global storage, ripen, visited
    directions=[(1,0,0),(-1,0,0),(0,1,0),(0,0,1),(0,-1,0),(0,0,-1)]
    new_ripen=deque()
    cnt=0
    while ripen:
        l, y, x=ripen.popleft()
        for di in directions:
            dl=l+di[0]
            dy=y+di[1]
            dx=x+di[2]
            if 0<=dl<h and 0<=dy<n and 0<=dx<m and visited[dl][dy][dx]==0:
                if storage[dl][dy][dx]==0:
                    storage[dl][dy][dx]=1
                    new_ripen.append((dl,dy,dx))
                    visited[dl][dy][dx]=1
                    cnt+=1
    ripen=new_ripen.copy()
    return cnt


change_tomato=0
# 모든 토마토가 익었는지 체크 -> 즉, 0에서 1로 바뀐 토마토의 개수가 초기 익은 토마토의 개수와 같으면 종료
time=0
while change_tomato<notripen:
    # 익은 토마토 전파
    change_tomato+=spread_ripen()
    # 더 이상 ripen에 남은 좌표가 없을 경우 -> 모든 토마토가 익는 것이 불가능한 경우
    if not ripen:
        print(-1)
        sys.exit(0)
    time+=1

print(time)
