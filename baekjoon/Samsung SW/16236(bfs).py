n=int(input())
# 0 빈칸
# 1-6 : 칸에 있는 물고기의 크기
# 9 : 아기 상어의 위치
fish=[list(map(int, input().split(' '))) for _ in range(n)]

size=2

babyshark=()
# 아기 상어 위치 찾기
for i in range(n):
    for j in range(n):
        if fish[i][j]==9:
            # 위치, time
            babyshark=(i,j)

# 현재 먹어야 하는 물고기를 찾는 bfs
directions=[(0,1),(1,0),(-1,0),(0,-1)]
def bfs():
    global fish
    min_x = 1e9
    min_y = 1e9
    min_dist = 1e9
    distance = [[0] * n for _ in range(n)]

    queue=[]
    queue.append(babyshark)
    visited=[[0]*n for _ in range(n)]
    visited[babyshark[0]][babyshark[1]]=1
    while queue:
        y,x=queue.pop(0)
        for di in directions:
            dy=y+di[0]
            dx=x+di[1]
            if 0<=dy<n and 0<=dx<n and visited[dy][dx]==0:
                if fish[dy][dx]<=size:
                    if fish[dy][dx]==size or fish[dy][dx]==0:
                        queue.append((dy,dx))
                        distance[dy][dx]=distance[y][x]+1
                        visited[dy][dx]=1
                    else:
                        queue.append((dy, dx))
                        visited[dy][dx] = 1
                        distance[dy][dx] = distance[y][x] + 1
                        # 최단 거리인지 체크
                        if distance[dy][dx] < min_dist:
                            min_dist = distance[dy][dx]
                            min_y=dy
                            min_x=dx
                        # 거리가 같다면
                        if distance[dy][dx] == min_dist:
                            # 가장 위쪽인지 체크
                            if dy < min_y:
                                min_y = dy
                                min_x = dx
                            # 같은 행이라면 가장 왼쪽인지 체크
                            elif dy == min_y:
                                if dx < min_x:
                                    min_x = dx
    return min_y, min_x, min_dist

eat_cnt=0
time=0
while True:
    min_y, min_x, min_dist = bfs()
    # 먹을 수 있는 물고기를 찾은 경우
    if min_x!=1e9 and min_y!=1e9:
        # 아기 상어가 있던 위치는 0으로 업데이트(이거 안해서 헤멤)
        fish[babyshark[0]][babyshark[1]]=0
        # 아기 상어의 위치를 물고기 먹은 위치로 이동
        babyshark = (min_y, min_x)
        # 먹은 물고기의 위치 갱신
        fish[min_y][min_x]=0
        # 해당 물고기를 먹으러 이동한 만큼 걸린 시간 추가
        time+=min_dist
        # 먹은 물고기 수가 사이즈와 동일해지면 size+=1
        eat_cnt+=1
        if eat_cnt==size:
            size+=1
            eat_cnt=0
    # 더 이상 먹을 물고기가 없으면
    else:
        print(time)
        break


















