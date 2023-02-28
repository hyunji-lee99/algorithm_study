import sys
from collections import deque

# 오답 ㅠㅠㅠ 다시 풀어봐야 함.


# n,t : 교차로 가로세로 길이, t시간 이내에 갈 수 있는 교차로 개수 구하기
# 각 교차로의 신호 집합이 주어진다.
# 신호는 항상 4개이며, 순서는 X축부터 진행을 한다.

n,t=map(int, sys.stdin.readline().strip().split(' '))
signs=[[[] for _ in range(n)] for _ in range(n)]

directionforsignal=[(-1,0),(0,1),(1,0),(0,-1)]
# 0 북, 1 동, 2 남, 3 서
# 방향 체크
signal=[[],[0,1,2,1], #1
        [3,0,1,0], #2
        [0,3,2,3], #3
        [0,2,1,2], #4
        [0,1,1], #5
        [3,0,0], #6
        [3,2,3], #7
        [2,1,2], #8
        [1,2,1], #9
        [0,1,0], #10
        [0,3,3], #11
        [3,2],2] #12

for i in range(n):
    for j in range(n):
        sign = list(map(int, sys.stdin.readline().strip().split(' ')))
        signs[i][j] = sign

#bfs - queue, visited, time, ablecross 초기화
queue=deque()
visited=[[[[0 for _ in range(4)] for _ in range(100)] for _ in range(n)] for _ in range(n)]
queue.append((0,0,0,0))
ablecrossCount=0
visited[0][0][0][0]=1

while queue:
    #현재 위치와 걸린 시간, 현재 이동 방향
    y,x,d,time=queue.popleft()
    visited[y][x][time][d] = 1
    if time>t:
        break
    else:
        ablecrossCount+=1
    timeforsignal=signal[signs[y][x][time%4]]
    #방향 체크
    direction=timeforsignal[-1]
    if d!=direction:
        continue
    for sign in timeforsignal[0:len(timeforsignal)-1]:
        dy=y+directionforsignal[sign][0]
        dx=x+directionforsignal[sign][1]

        if 0<=dy<n and 0<=dx<n and visited[dy][dx][time][sign]==0:
            queue.append((dy,dx,sign,time+1))


print(ablecrossCount)