import sys
from collections import deque

n,m=map(int, sys.stdin.readline().split(' '))

route=[]
for _ in range(m):
    a,b,c=map(int, sys.stdin.readline().split(' '))
    route.append((a,b,c))

dist=[1e9]*(n+1)
dist[1]=0

for v in range(n):
    for s,e,w in route:
        if dist[s]!=1e9 and dist[e]>dist[s]+w:
            if v==n-1:
                print(-1)
                sys.exit(0)
            dist[e]=dist[s]+w

for d in dist[2:n+1]:
    if d!=1e9:
        print(d)
    else:
        print(-1)









