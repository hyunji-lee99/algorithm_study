import sys
from collections import deque

t=int(sys.stdin.readline())
gear=[list(map(int, list(sys.stdin.readline().strip()))) for _ in range(t)]
# dummy
gear.insert(0,[])

def rotate(num, dir):
    global gear
    # 반시계
    if dir==-1:
        tmp=gear[num].pop(0)
        gear[num].append(tmp)
    # 시계
    elif dir==1:
        tmp=gear[num].pop()
        gear[num].insert(0,tmp)


k=int(sys.stdin.readline())
for _ in range(k):
    number, direction=map(int, sys.stdin.readline().split(' '))
    queue=deque()
    queue.append((number,direction))
    visited=[0]*(t+1)
    while queue:
        num,dir=queue.popleft()
        # num 기준 왼쪽에 있는 톱니바퀴와 맞닿은 극이 다른 경우
        if 1<=num-1<=t and gear[num-1][2]!=gear[num][6] and visited[num-1]==0:
            if dir==-1:
                queue.append((num-1,1))
            elif dir==1:
                queue.append((num-1,-1))
        if 1<=num+1<=t and gear[num+1][6]!=gear[num][2] and visited[num+1]==0:
            if dir==-1:
                queue.append((num+1,1))
            elif dir==1:
                queue.append((num+1,-1))
        rotate(num,dir)
        visited[num]=1

ans=0
for i in range(1,t+1):
    if gear[i][0]==1:
        ans+=1

print(ans)



