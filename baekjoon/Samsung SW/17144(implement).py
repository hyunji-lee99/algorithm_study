
r,c,t=map(int, input().split(' '))

area=[]
for i in range(r):
    tmp=list(map(int, input().strip().split(' ')))
    area.append(tmp)

# 공기청정기 위치 저장
for i in range(r):
    for j in range(c):
        if area[i][j]==-1:
            up_conditioner=i-1
            down_conditioner=i
            break

def bfs():
    global area, up_conditioner, down_conditioner
    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    dust=[]
    # 시간 체크
    cnt=1
    while cnt<=t:
        # 미세먼지 현황 체크
        for i in range(r):
            for j in range(c):
                if area[i][j] > 0:
                    dust.append((i, j, area[i][j]))
        # 미세먼지 확산
        while dust:
            y, x, v  = dust.pop(0)
            for dir in directions:
                dy = y + dir[0]
                dx = x + dir[1]
                # 범위 안이면서 공기청정기가 있는 곳이 아니면
                if 0 <= dy < r and 0 <= dx < c and area[dy][dx] != -1:
                    spread = v // 5
                    area[y][x]-=spread
                    area[dy][dx] += spread
        # 공기청정기 작동
        # 공기청정기에서 가까운 쪽부터 연산
        # 위쪽 공기청정기(반시계방향 순환)
        # 중 아래쪽 방향
        # 공기청정기 바로 위부터 0행까지 탐색
        for i in range(up_conditioner-1,-1,-1):
            if area[i][0]>0:
                # 바로 밑 칸이 공기청정기면 정화되었다치고, 해당 칸 0으로(이걸 놓쳐서 계속 오답이 발생했었음)
                if area[i+1][0]==-1:
                    area[i][0]=0
                else:
                    area[i + 1][0] = area[i][0]
                    area[i][0] = 0
        # 중 왼쪽 방향
        # 맨 왼쪽부터 오른쪽 끝까지
        for i in range(1, c):
            if area[0][i]>0:
                area[0][i-1]=area[0][i]
                area[0][i]=0
        # 중 위쪽 방향
        # 맨 위쪽부터 공기청정기가 존재하는 행까지
        for i in range(1, up_conditioner+1):
            if area[i][c-1]>0:
                area[i-1][c-1]=area[i][c-1]
                area[i][c-1]=0
        # 중 오른쪽 방향
        # 맨 오른쪽부터 왼쪽 끝까지
        for i in range(c-2, 0,-1):
            if area[up_conditioner][i]>0:
                area[up_conditioner][i+1]=area[up_conditioner][i]
                area[up_conditioner][i]=0

        # 아래쪽 공기청정기(시계방향)
        # 중 위쪽 방향
        # 공기청정기가 존재하는 행부터 맨 아래까지
        for i in range(down_conditioner + 1, r):
            if area[i][0] > 0:
                # 바로 위 칸이 공기청정기면
                if area[i-1][0]==-1:
                    area[i][0]=0
                else:
                    area[i - 1][0] = area[i][0]
                    area[i][0] = 0
        # 중 왼쪽 방량
        # 맨 왼쪽부터 오른쪽까지
        for i in range(1, c):
            if area[r-1][i]>0:
                area[r-1][i-1]=area[r-1][i]
                area[r-1][i]=0
        # 중 아래쪽 방향
        # 맨 아래부터 공기청정기가 존재하는 행까지
        for i in range(r-2, down_conditioner-1,-1):
            if area[i][c-1]>0:
                area[i+1][c-1]=area[i][c-1]
                area[i][c-1]=0
        # 중 오른쪽 방향
        # 맨 오른쪽부터 맨 왼쪽까지
        for i in range(c-2, 0,-1):
            if area[down_conditioner][i]>0:
                area[down_conditioner][i+1]=area[down_conditioner][i]
                area[down_conditioner][i]=0
        # 시간 추가
        cnt+=1

bfs()

# 남은 미세먼지 양 계산
ans=0
for i in range(r):
    for j in range(c):
        if area[i][j]>0:
            ans+=area[i][j]

print(ans)

