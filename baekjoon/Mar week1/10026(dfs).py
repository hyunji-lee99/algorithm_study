#적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.
#적록색약은 빨강과 초록을 구분하지 못함

import sys
sys.setrecursionlimit(10**6)

n=int(sys.stdin.readline())
picture=[]
for i in range(n):
    tmp=list(sys.stdin.readline().strip())
    picture.append(tmp)


def dfs(i,j,color):
    directions=[(0,1),(1,0),(-1,0),(0,-1)]
    visited[i][j]=1
    for di in directions:
        dx=j+di[0]
        dy=i+di[1]
        if 0<=dx<n and 0<=dy<n and picture[dy][dx]==color and visited[dy][dx]==0:
            dfs(dy,dx,color)

#적록색약이 아닌 경우
visited=[[0]*(n) for _ in range(n)]
notweakness=0
for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            dfs(i, j, picture[i][j])
            notweakness+=1

#적록색약인 경우

for i in range(n):
    for j in range(n):
        if picture[i][j]=='R':
            picture[i][j]='G'


visited=[[0]*(n) for _ in range(n)]
weakness=0
for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            dfs(i, j, picture[i][j])
            weakness+=1

print(notweakness, weakness)
