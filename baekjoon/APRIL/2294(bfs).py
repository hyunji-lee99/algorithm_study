import sys
from collections import deque

n,k=map(int, sys.stdin.readline().split(' '))
coin=[int(sys.stdin.readline()) for _ in range(n)]

coin.sort(reverse=True)

# init
queue=deque()
for c in coin:
    # 코인 값, 개수
    queue.append((c,1))

visited=[0]*100001
while queue:
    result, num=queue.popleft()
    if result==k:
        print(num)
        break
    for c in coin:
        if result+c<=k and visited[result+c]==0:
            queue.append((result+c, num+1))
            visited[result+c]=1
else:
    print(-1)
