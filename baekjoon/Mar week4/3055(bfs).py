# 불이랑 비슷한 문제
import sys
from collections import deque

r,c=map(int, sys.stdin.readline().split(' '))
area=[list(sys.stdin.readline().strip()) for _ in range(r)]

# 물과 도치 위치 찾기
water=deque()
doci=deque()

for i in range(r):
    for j in range(c):
        if area[i][j]=='*':
            water.append((i,j))
        elif area[i][j]=='S':
            doci.append((i,j))


cnt=0
while doci:
    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    # 물 퍼트리기
    # popleft를 사용하면 new배열도 deque로 선언
    new_water=deque()
    visited_water=[[0]*c for _ in range(r)]
    visited_doci = [[0] * c for _ in range(r)]
    while water:
        y,x=water.popleft()
        for di in directions:
            dy=y+di[1]
            dx=x+di[0]
            if 0<=dy<r and 0<=dx<c and visited_water[dy][dx]==0 and (area[dy][dx]=='.' or area[dy][dx]=='S'):
                new_water.append((dy,dx))
                visited_water[dy][dx]=1
                area[dy][dx]='*'
    # 새로운 water 리스트로 업데이트
    water=new_water.copy()
    # 고슴도치 이동시키기
    # 시간대별로 구분해야 하기 때문에 new 배열에 담아서 현재 담고 있는 원소들을 모두 탐색하고 마지막에 업데이트
    new_doci=deque()
    while doci:
        y,x=doci.popleft()
        if area[y][x]=='D':
            print(cnt)
            sys.exit(0)
        for di in directions:
            dy=y+di[1]
            dx=x+di[0]
            if 0<=dy<r and 0<=dx<c and visited_doci[dy][dx]==0 and (area[dy][dx]=='.' or area[dy][dx]=='D'):
                new_doci.append((dy,dx))
                visited_doci[dy][dx]=1
    doci=new_doci.copy()
    cnt+=1

# while문 안에서 종료되지 않았다는 것은 비버의 굴로 들어갈 수 없다는 것
print('KAKTUS')