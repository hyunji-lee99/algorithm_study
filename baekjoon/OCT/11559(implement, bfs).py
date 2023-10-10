import sys
from collections import deque

field=[[] for _ in range(6)]
# 12개의 행으로 이루어진 필드가 아니라, 열을 기준으로 6개의 행으로 필드를 만듦(field 업데이트를 pop으로 간단하게 하기 위해서)
for _ in range(12):
    line=list(sys.stdin.readline().strip())
    for idx in range(6):
        field[idx].append(line[idx])

def field_update(visited):
    global field
    for i in range(6):
        for j in range(12):
            if visited[i][j]==1:
                field[i].pop(j)
                field[i].insert(0,'.')

def BFS(i,j):
    global visited
    queue=deque()
    queue.append((i,j))
    visited[i][j]=1
    delete_list = []
    delete_list.append((i,j))

    color=field[i][j]
    directions=[(0,1),(1,0),(0,-1),(-1,0)]

    while queue:
        y,x=queue.popleft()
        for di in directions:
            dy=y+di[0]
            dx=x+di[1]
            if 0<=dy<6 and 0<=dx<12 and visited[dy][dx]==0 and field[dy][dx]==color:
                queue.append((dy,dx))
                visited[dy][dx]=1
                delete_list.append((dy,dx))
    if len(delete_list)>=4:
        return True
    else:
        # 연쇄가 일어나지 않았다면 visited 원상 복구
        for y,x in delete_list:
            visited[y][x]=0
        return False

ans=0
repeat=True
while repeat:
    isProcessed = False
    visited = [[0] * 12 for _ in range(6)]
    for i in range(6):
        for j in range(12):
            if field[i][j] != '.' and visited[i][j]==0:
                if BFS(i,j):
                    isProcessed=True
    # 모든 위치 탐색해도 BFS가 True가 안나오는 경우
    if isProcessed==False:
        repeat=False
    else:
        # 1 연쇄가 끝나면 field update
        field_update(visited)
        ans+=1

print(ans)
