import sys
from collections import deque

N, T, G=map(int, sys.stdin.readline().split(' '))

# queue, visited init
queue=deque()
queue.append((N,0))
visited=[0]*100000
visited[N]=1

while queue:
    cur,cnt=queue.popleft()
    # cur값이 G값인 것을 확인하는 것보다 시같 초과로 인한 탈출 조건을 먼저 확인해줘야 함!
    # 이거때문에 계속 틀림. 이유는? -> 버튼을 누른 횟수가 초과한 다음에 G값과 동일해질 수도 있기 때문에, 먼저 T회를 넘어서지 않았는지 먼저 확인해야 함.
    # 버튼을 누른 횟수가 T 초과하면 종료
    if cnt > T:
        print('ANG')
        break
    # G값이 되면 종료
    if cur==G:
        print(cnt)
        break
    # A 버튼을 누른 경우
    A=cur+1
    if A>99999:
        continue
    else:
        if visited[A] == 0:
            queue.append((A, cnt + 1))
            visited[A] = 1

    # B 버튼을 누른 경우(B가 0보다 큰 경우만)
    if cur>0:
        B = 2 * cur
        if B > 99999:
            # 초과하면 바로 탈출 실패가 아니라, 해당 케이스를 확인하지 마라
            continue
        else:
            n = len(str(B)) - 1
            B -= 10 ** n
            if visited[B] == 0:
                queue.append((B, cnt + 1))
                visited[B] = 1
else:
    print('ANG')
