import sys
from collections import deque

m,n=map(int, sys.stdin.readline().split(' '))
tomato=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]

# 현재 익은 토마토의 위치와 현재 시간을 큐에 저장
# 빈 칸 인 경우 저장
ripen_tomato=deque()
not_exist=0
for i in range(n):
    for j in range(m):
        if tomato[i][j]==1:
            ripen_tomato.append((i,j,0))
        elif tomato[i][j]==-1:
            not_exist+=1

# 처음부터 모든 토마토가 익어있는 경우 0 출력하고 종료
num_of_ripen_tomato=len(ripen_tomato)
if num_of_ripen_tomato==(m*n-not_exist):
    print(0)
    sys.exit(0)


def spread_ripe():
    global ripen_tomato, time
    directions=[(1,0),(0,1),(-1,0),(0,-1)]
    #visited=[[0]*m for _ in range(n)]
    add_ripen_tomato=0
    while ripen_tomato and ripen_tomato[0][2]==time:
        y, x, t=ripen_tomato.popleft()
        for di in directions:
            dy=y+di[0]
            dx=x+di[1]
            if 0<=dy<n and 0<=dx<m and tomato[dy][dx]==0:
                tomato[dy][dx]=1
                ripen_tomato.append((dy,dx,t+1))
                add_ripen_tomato+=1

    if add_ripen_tomato:
        return add_ripen_tomato
    else:
        return 0

time=0
while num_of_ripen_tomato<(n*m-not_exist):
    # 익은 토마토와 인접한 익지 않은 토마토로 전파
    add_tomato=spread_ripe()
    if add_tomato==0:
        print(-1)
        sys.exit(0)
    num_of_ripen_tomato+=add_tomato
    time+=1

print(time)






