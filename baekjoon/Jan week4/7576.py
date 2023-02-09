#m : 상자의 가로 칸 수
#n : 상자의 세로 칸 수

#bfs를 사용했어야 함 -> 단순 for문 구현으로 풀면 시간초과 발생
#전체 탐색보단 1인 경우만 큐에 넣어서 탐색해야 함
#수정중
import sys
from collections import deque

m,n=map(int, sys.stdin.readline().split(' '))
tomato=[]
for i in range(n):
    tmp=list(map(int, sys.stdin.readline().split(' ')))
    tomato.append(tmp)

visited=[[0 for _ in range(m)] for _ in range(n)]
visited_minus=[[0 for _ in range(m)] for _ in range(n)]
di=[(0,1),(1,0),(0,-1),(-1,0)]

#0이 남을 수 밖에 없는 경우(어떤 0을 -1로 둘러싼 경우), 모든 토마토가 익은 상태인 경우는 미리 필터링
#모두 익어있는 경우
#2차원 배열에서 특정 원소 포함여부 찾기 주의
if all(0 not in l for l in tomato):
    print(0)
    sys.exit(0)

#익을 수 없는 토마토가 있는 경우(어떤 0을 -1로 둘러싼 부분이 있는 경우)
#행렬 인덱스 처리할 때, 가로세로 주의
for i in range(n):
    for j in range(m):
        #-1이 아닌 수가 있는 경우
        if tomato[i][j]==0 and visited_minus[i][j]==0:
            visited_minus[i][j]=1
            ifminus = -1
            for d in di:
                dx = i + d[0]
                dy = j + d[1]
                if 0 <= dx < n and 0 <= dy < m and tomato[dx][dy] != -1:
                    ifminus = 1
            if ifminus == -1:
                print(-1)
                sys.exit(0)

#토마토 지도를 상하좌우 탐색하면서 1인 경우, 상하좌우에 위치한 원소를 1로 바꿔주면서 변화시켜줌. 날짜는 1턴마다 counting
#visited 배열에 방문했던 곳인지 기록해서 방문했던 곳인 경우 패스
#0이 남아있지 않을 때까지 반복
day=0
while any(0 in l for l in tomato):
    change=[]
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 1 and visited[i][j]==0:
                visited[i][j]=1
                for d in di:
                    dx = i + d[0]
                    dy = j + d[1]
                    if 0 <= dx < n and 0 <= dy < m and tomato[dx][dy] == 0:
                        change.append((dx,dy))
    for x,y in change:
        tomato[x][y]=1
    day+=1

print(day)