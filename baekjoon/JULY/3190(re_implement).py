import sys
from collections import deque

# 정사각판 크기
n=int(sys.stdin.readline())
# 사과의 개수
k=int(sys.stdin.readline())

# 사과의 위치
apple=[[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    i,j=map(int, sys.stdin.readline().split(' '))
    apple[i][j]=1

# 뱀의 방향 변환 횟수
l=int(sys.stdin.readline())
change_direction=[0]*10001
for _ in range(l):
    second, dir=sys.stdin.readline().strip().split(' ')
    change_direction[int(second)]=dir

snake=[[0]*(n+1) for _ in range(n+1)]
# 뱀은 처음에 맨 위 좌측에서 길이 1로 시작하며, 처음에 오른쪽으로 이동함
snake[1][1]=1
# snake_index[0]이 뱀 머리 좌표, snake_index[-1]이 뱀 꼬리 좌표
snake_index=deque([(1,1)])
# 상 우 하 좌
directions=[(-1,0),(0,1),(1,0),(0,-1)]
cur_dir=1

time=1
while True:
    dy, dx = snake_index[0][0] + directions[cur_dir][0], snake_index[0][1] + directions[cur_dir][1]
    if 1 <= dy <= n and 1 <= dx <= n and snake[dy][dx]==0:
        snake[dy][dx] = 1
        snake_index.appendleft((dy,dx))
        # 사과가 없으면
        if apple[dy][dx] == 0:
            snake[snake_index[-1][0]][snake_index[-1][1]] = 0
            snake_index.pop()
        # 사과가 있으면
        else:
            # 사과 제거
            apple[dy][dx]=0
    else:
        # 벽에 부딪히거나 자기 자신과 부딪힘
        print(time)
        sys.exit(0)
    # 방향 변환해야 하는지 확인
    if change_direction[time]=='L':
        cur_dir=(cur_dir+3)%4
    elif change_direction[time]=='D':
        cur_dir=(cur_dir+1)%4
    time+=1





