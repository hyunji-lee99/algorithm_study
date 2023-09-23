import sys
from collections import deque

A,B,C=map(int, sys.stdin.readline().strip().split(' '))

queue=deque()
queue.append((0,0,C))
visited=set()
ans=[]
while queue:
    a,b,c=queue.popleft()
    if (a,b,c) in visited:
        continue
    visited.add((a, b, c))
    if a==0:
        ans.append(c)
    # 1->2
    if a+b>B:
        # 1->2로 물을 부을 때 2의 용량을 초과하는 경우
        queue.append((a+b-B, B, c))
    else:
        queue.append((0,a+b,c))
    # 1->3
    if a+c>C:
        queue.append((a+c-C,b,C))
    else:
        queue.append((0,b,a+c))
    # 2->1
    if a+b>A:
        queue.append((A,a+b-A,c))
    else:
        queue.append((a+b, 0,c))
    # 2->3
    if b+c>C:
        queue.append((a, b+c-C,C))
    else:
        queue.append((a, 0, b+c))
    # 3->1
    if a+c>A:
        queue.append((A, b, a+c-A))
    else:
        queue.append((a+c, b, 0))
    # 3->2
    if b+c>B:
        queue.append((a,B,b+c-B))
    else:
        queue.append((a,b+c,0))

ans.sort()
print(*ans, sep=' ')