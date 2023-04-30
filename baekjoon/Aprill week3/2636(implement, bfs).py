import sys
from collections import deque

n,m=map(int, sys.stdin.readline().split(' '))

area=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]

# 시간 체크
time=0
# 한 시간 후에 사라질 치즈 기록
melting=[]
# 시간별로 사라진 치즈 수 기록
delete_cheese=[]

# 치즈가 모두 녹았는지 파악하기 위한 초기 치즈의 개수
init_cheese=0
for i in range(n):
    for j in range(m):
        if area[i][j]==1:
            init_cheese+=1
# 현재 치즈가 몇 개 녹았는지 체크
cur_cheese=0
def check_melt():
    # bfs를 이용해서 외부공기인 0인 인덱스를 기준으로 인접한 곳에 1이 있는 탐색하는 방식
    # 1이면 한 시간 뒤에 녹여햐 하는 치즈로 표시
    # 0이면 큐에 넣어서 탐색용으로 사용해야 함
    global melting, area, cur_cheese
    queue=deque()
    visited = [[0] * (m) for _ in range(n)]
    queue.append((0,0))
    visited[0][0]=1
    directinos=[(1,0),(0,1),(-1,0),(0,-1)]
    while queue:
        y,x=queue.popleft()
        for di in directinos:
            dy=y+di[0]
            dx=x+di[1]
            if 0<=dy<n and 0<=dx<m and visited[dy][dx]==0:
                if area[dy][dx]==1:
                    melting.append((dy,dx))
                    cur_cheese+=1
                    visited[dy][dx]=1
                elif area[dy][dx]==0:
                    queue.append((dy,dx))
                    visited[dy][dx]=1

    delete_cheese.append(cur_cheese)

def melting_cheese():
    global area, melting
    for y,x in melting:
        area[y][x]=0

# 현재 녹은 치즈의 개수가 초기 치즈의 개수보다 작을 동안 반복
while cur_cheese<init_cheese:
    # 한 시간 뒤에 어떤 치즈가 녹아야 하는지 체크
    check_melt()
    # 치즈 녹임
    melting_cheese()
    time+=1

# 치즈가 모두 녹을 때까지 걸린 시간
print(time)
# 치즈가 모두 녹기 한 시간 전에 남은 치즈의 개수
# 95%에서 틀림 -> 1시간만에 모두 녹는 경우 반례
if time==1:
    print(init_cheese)
else:
    print(init_cheese-delete_cheese[len(delete_cheese)-2])

