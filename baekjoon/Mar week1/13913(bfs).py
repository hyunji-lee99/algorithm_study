# 숨바꼭질4
# 경로를 저장하는 방식을 배울 수 있음!

import sys
from collections import deque

n,k=map(int, sys.stdin.readline().split(' '))
queue=deque()
visited=[0]*100001
parent=[0]*100001
queue.append((n,0))

while queue:
    cur,time=queue.popleft()
    if cur==k:
        ans=[]
        print(time)
        p=cur
        while p!=n:
            ans.append(p)
            p=parent[p]
        ans.append(n)
        for i in range(len(ans)-1,-1,-1):
            print(ans[i], end=' ')
        break
    for idx in (cur-1,cur+1,2*cur):
        if 0<=idx<100001 and visited[idx]==0:
            queue.append((idx, time+1))
            visited[idx]=1
            parent[idx] = cur


