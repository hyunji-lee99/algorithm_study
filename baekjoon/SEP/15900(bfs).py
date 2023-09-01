# 이동 거리가 홀수여야 성원이가 이길 수 있다.
import sys
from collections import deque

# sys.setrecursionlimit(10**5)

n=int(sys.stdin.readline())
tree=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int, sys.stdin.readline().split(' '))
    tree[a].append(b)
    tree[b].append(a)

# def dfs(cur, parent, depth):
#     global ans
#     # 연결된 노드가 하나이고, 그 연결된 노드가 부모일 경우 그 노드는 리프 노드
#     if len(tree[cur])==1 and tree[cur][0]==parent:
#         ans+=depth
#         return
#     for node in tree[cur]:
#         if node==parent:
#             continue
#         dfs(node, cur, depth+1)

ans=0
def bfs(cur, parent, depth):
    global ans
    queue=deque()
    queue.append((cur, parent, depth))
    while queue:
        c, p, d=queue.popleft()
        # 리프 노드인가?
        if len(tree[c])==1 and tree[c][0]==p:
            ans+=d
            continue
        for node in tree[c]:
            if node!=p:
                queue.append((node, c, d+1))

#dfs(1, -1, 0)
bfs(1,-1,0)

if ans%2==1:
    print('Yes')
else:
    print('No')