import sys
from collections import deque

R,C,N=map(int, sys.stdin.readline().strip().split(' '))
bomber=[list(sys.stdin.readline().strip()) for _ in range(R)]

bomber_queue=deque()
# 초기 상태의 폭탄 위치와 시간 저장
for i in range(R):
    for j in range(C):
        if bomber[i][j]=='O':
            bomber_queue.append((i,j,0))

def install_bomber(time):
    global bomber, bomber_queue
    for i in range(R):
        for j in range(C):
            if bomber[i][j]=='.':
                bomber[i][j]='O'
                bomber_queue.append((i,j,time))

def boom(time):
    global bomber, bomber_queue
    directions=[(0,1),(1,0),(-1,0),(0,-1)]
    # bomber_queue에 요소가 존재하는 경우 조건 추가해야 인덱스 에러 발생하지 않음.
    while bomber_queue and bomber_queue[0][2]==(time-3):
        y,x,t=bomber_queue.popleft()
        bomber[y][x]='.'
        for dy, dx in directions:
            newy=y+dy
            newx=x+dx
            if 0<=newy<R and 0<=newx<C and bomber[newy][newx]=='O':
                bomber[newy][newx]='.'
    # 새로운 bomber queue 업데이트
    new_bomber_queue=deque()
    while bomber_queue:
        y,x,t=bomber_queue.popleft()
        if bomber[y][x]=='O':
            new_bomber_queue.append((y,x,t))

    bomber_queue=new_bomber_queue.copy()

# 처음에 폭탄 설치하고 1초간 아무것도 안함. 2초부터 행동
time=2
while time<=N:
    # 폭탄이 설치되지 않은 칸에 폭탄 설치
    install_bomber(time)
    # 1초가 지난 후 3초 전에 설치된 폭탄 모두 폭발
    time+=1
    if time>N:
        break
    boom(time)
    time+=1

for i in range(R):
    for j in range(C):
        print(bomber[i][j],end='')
    print('')
