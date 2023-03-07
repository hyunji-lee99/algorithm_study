#숨바꼭질2

import sys
from collections import deque

n,k=map(int, sys.stdin.readline().split(' '))

queue=deque()
queue.append((n,0))
visited=[0]*100001

minvalue=0
#가장 적게 시간이 걸리는 값인지 체크용
first=0
ans=0
while queue:
    cur,time=queue.popleft()
    visited[cur]=1
    if cur==k:
        if first==0:
            minvalue = time
            first = 1
            ans+=1
        elif time==minvalue:
            ans+=1
    for dn in (cur+1,cur-1,2*cur):
        if 0<=dn<=100000 and visited[dn]==0:
            queue.append((dn, time+1))

print(minvalue)
print(ans)