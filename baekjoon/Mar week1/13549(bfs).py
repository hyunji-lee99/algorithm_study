#숨바꼭질3

import sys
from collections import deque

n,k=map(int, sys.stdin.readline().split(' '))

visited=[0]*100001
queue=deque()
queue.append((n,0))
visited[n]=1
ans=1e9
while queue:
    cur,time=queue.popleft()
    visited[cur]=1
    if cur==k:
        ans = min(ans, time)
    for i,t in ((cur+1,1),(cur-1,1),(2*cur,0)):
        if 0<=i<100001 and visited[i]==0:
            queue.append((i,time+t))

print(ans)