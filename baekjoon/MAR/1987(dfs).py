# 백트래킹 + dfs
import sys

r,c=map(int, sys.stdin.readline().split(' '))

map=[]
for i in range(r):
    tmp=list(sys.stdin.readline().strip())
    map.append(tmp)

#알파벳 개수
visited = [0]*26
ans=0
directions=[(0,1),(0,-1),(1,0),(-1,0)]

def dfs(y,x,cnt):
    global ans
    ans=max(ans,cnt)
    for di in directions:
        dy=y+di[1]
        dx=x+di[0]
        if 0<=dy<r and 0<=dx<c and visited[ord(map[dy][dx])-ord('A')]==0:
            visited[ord(map[dy][dx]) - ord('A')] = 1
            dfs(dy,dx,cnt+1)
            visited[ord(map[dy][dx]) - ord('A')] = 0

visited[ord(map[0][0])-ord('A')]=1
dfs(0,0,1)

print(ans)

#bfs는 메모리 초과
# while queue:
#     y,x,cnt,visited=queue.popleft()
#     ans=max(ans,cnt)
#     visited[ord(map[y][x])-ord('A')]=1
#     for di in directions:
#         dy=y+di[1]
#         dx=x+di[0]
#         if 0 <= dy < r and 0 <= dx < c and visited[ord(map[dy][dx])-ord('A')]==0:
#             queue.append((dy, dx, cnt + 1, visited.copy()))
