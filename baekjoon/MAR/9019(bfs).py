import sys
from collections import deque

# t는 테스트케이스의 개수
t=int(sys.stdin.readline())

def bfs(a,b):
    # queue, visited init
    queue=deque()
    visited=[0]*10000
    queue.append((a,''))
    visited[a]=1

    while queue:
        cur, command = queue.popleft()
        if cur==b:
            return command
        # D 명령 수행(n을 두 배, 결과 값이 9999보다 크면 10000으로 나눈 나머지 저장)
        if 2*cur>9999:
            D=(2*cur)%10000
        else:
            D=2*cur
        if visited[D]==0:
            queue.append((D, command+'D'))
            visited[D]=1

        # S 명령 수행(n-1, n이 0이면 9999 저장)
        if cur>0:
            S=cur-1
        else:
            S=9999
        if visited[S]==0:
            queue.append((S, command+'S'))
            visited[S]=1

        # L 명령어 수행(왼쪽으로 각 자릿수 이동)
        # 단순히 cur을 str로 표현하는 것이 아니라, 앞 자릿수에 0을 붙여야 함. 예를 들어, 5 -> '5'가 아니라, 5-> '0005'
        str_cur=str(cur)
        if len(str_cur)<4:
            str_cur='0'*(4-len(str_cur))+str_cur
        left_str_cur=str_cur[1:]+str_cur[0]
        L=int(left_str_cur)
        if visited[L]==0:
            queue.append((L, command+'L'))
            visited[L]=1

        # R 명령어 수행(오른쪽으로 각 자릿수 이동)
        right_str_cur=str_cur[-1]+str_cur[:-1]
        R=int(right_str_cur)
        if visited[R]==0:
            queue.append((R, command+'R'))
            visited[R]=1

for i in range(t):
    a,b=map(int, sys.stdin.readline().split(' '))
    print(bfs(a,b))
