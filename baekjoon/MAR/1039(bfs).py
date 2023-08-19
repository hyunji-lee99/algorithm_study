import sys
from collections import deque

n,k=map(int, sys.stdin.readline().strip().split(' '))

visited=set()
queue=deque()
# 같은 시간대에 방문한 적이 있는 string인지 확인해줘야 함.
# 그렇지 않으면 이전에 방문한 string이라는 이유로 k 시간 이후에 만들 수 있는 string의 최대값을 탐색할 수 없음
visited.add((str(n),0))
queue.append((str(n),0))
maxvalue=0
while queue:
    string, time=queue.popleft()
    if time>k:
        print(maxvalue)
        break
    if time==k:
        maxvalue=max(maxvalue, int(string))
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            # swap
            copy_string=list(string[:])
            tmpi=string[i]
            tmpj=string[j]
            copy_string[i]=tmpj
            copy_string[j]=tmpi
            copy_string=''.join(copy_string)
            # 바뀐 수가 '0'으로 시작하면 안됨
            if copy_string[0]!='0':
                if (copy_string, time + 1) not in visited:
                    visited.add((copy_string, time + 1))
                    queue.append((copy_string, time + 1))
else:
    print(-1)
