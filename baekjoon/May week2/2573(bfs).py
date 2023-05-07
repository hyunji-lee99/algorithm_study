import sys
from collections import deque

n,m=map(int, sys.stdin.readline().split(' '))
ice=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]

ice_info=deque()
init_ice_number=0
for i in range(n):
    for j in range(m):
        if ice[i][j]>0:
            ice_info.append((i,j,ice[i][j]))
            init_ice_number+=1

def melt_ice():
    global ice, ice_info
    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    new_ice_info=deque()
    copy_ice=[arr[:] for arr in ice]
    melted_ice_cnt=0
    while ice_info:
        y,x,value=ice_info.popleft()
        sea_cnt=0
        for di in directions:
            dy=y+di[0]
            dx=x+di[1]
            if 0<=dy<n and 0<=dx<m:
                # 주변에 감싸고 있는 0의 개수가 몇 개인지 확인
                if ice[dy][dx]==0:
                    sea_cnt+=1
        if value-sea_cnt<=0:
            copy_ice[y][x]=0
            melted_ice_cnt+=1
        else:
            copy_ice[y][x]=value-sea_cnt
            new_ice_info.append((y,x,value-sea_cnt))

    ice_info=new_ice_info.copy()
    ice=[arr[:] for arr in copy_ice]
    return melted_ice_cnt

def isMoreThanTwo():
    global ice
    queue=deque()
    check_ice=[arr[:] for arr in ice]
    directions=[(1,0),(0,1),(-1,0),(0,-1)]
    cnt=0
    for i in range(n):
        for j in range(m):
            if check_ice[i][j]>0:
                cnt+=1
                queue.append((i,j))
                check_ice[i][j]=0
                while queue:
                    y,x=queue.popleft()
                    for di in directions:
                        dy=y+di[0]
                        dx=x+di[1]
                        if 0<=dy<n and 0<=dx<m and check_ice[dy][dx]>0:
                            queue.append((dy,dx))
                            check_ice[dy][dx]=0

    return cnt



melted_ice=0
time=1
while melted_ice<init_ice_number:
    # 얼음 녹이고, 녹은 개수 리턴
    melted_ice+=melt_ice()
    if isMoreThanTwo()>=2:
        print(time)
        break
    time+=1
else:
    print(0)



