import sys
from collections import deque

n,m=map(int, sys.stdin.readline().split(' '))
area=[list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(n)]

dpLeft=[[0]*m for _ in range(n)]
dpRight=[[0]*m for _ in range(n)]
dpRight[0][0]=area[0][0]
dpLeft[0][0]=area[0][0]

# 첫 번째 시작 부분에선 왼쪽, 오른쪽 중 오른쪽으로 밖에 갈 수 없으므로, area를 왼->오 방향으로 변경
for i in range(1,m):
    area[0][i]+=area[0][i-1]


for i in range(1, n):
    # dpRight[i][0]은 위에서 내려오는 한 가지 경우만 가능
    dpRight[i][0] = area[i-1][0] + area[i][0]
    # dpLeft[i][-1]은 위에서 내려오는 한 가지 경우만 가능
    dpLeft[i][-1] = area[i-1][-1] + area[i][-1]
    # 오른쪽 방향으로 가는 경우
    for j in range(1,m):
        # 왼쪽에서 오는 방향와 아래에서 내려오는 방향 중 어디가 더 큰지 확인
        dpRight[i][j]=area[i][j]+max(area[i-1][j], dpRight[i][j-1])
    # 왼쪽 방향으로 가는 경우
    for j in range(m-2,-1,-1):
        # 오른쪽에서 오는 방향과 내려오는 방향 중 어디가 더 큰지 확인
        dpLeft[i][j]=area[i][j]+max(area[i-1][j], dpLeft[i][j+1])
    # dpLeft, dpRight 중 어느 값이 더 큰지 비교
    for j in range(m):
        area[i][j]=max(dpLeft[i][j], dpRight[i][j])

    for a in area:
        print(a)
    print('')

print(area[-1][-1])

