import sys
from collections import deque

t,a,b=map(int, sys.stdin.readline().split(' '))

queue=deque([(0,0)])
ans=-1e9
visited=[[0]*(2) for _ in range(t+1)]
visited[0][0]=1
# 0 => not drunk
# 1 => drunk
while queue:
    cur, isDrunk=queue.popleft()
    ans=max(ans, cur)
    # eat orange
    if cur+a<=t and visited[cur+a][isDrunk]==0:
        queue.append((cur+a,isDrunk))
        visited[cur+a][isDrunk]=1
    # eat lemon
    if cur+b<=t and visited[cur+b][isDrunk]==0:
        queue.append((cur+b, isDrunk))
        visited[cur+b][isDrunk]=1
    # drink water
    if not isDrunk and visited[cur//2][not isDrunk]==0:
        queue.append((cur//2, 1))
        visited[cur//2][not isDrunk]=1

print(ans)