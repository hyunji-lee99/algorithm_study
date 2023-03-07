# m,n : 세로, 가로 길이
# k : 직사각형의 개수
# 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x,y좌표값과 오른쪽 위 꼭짓점의 x,y 좌표값이 주어짐
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

m,n,k=map(int, sys.stdin.readline().strip().split(' '))
area=[[0]*(n) for _ in range(m)]

# 칠해진 영역은 1, 빈 영역은 0으로 표현
for i in range(k):
    x1,y1,x2,y2=map(int, sys.stdin.readline().strip().split(' '))
    for x in range(x1,x2):
        for y in range(m-y2, m-y1):
            if area[y][x]==0:
                area[y][x]=1

visited=[[0]*(n) for _ in range(m)]
#dfs
def dfs(i,j):
    global width
    directions=[(0,-1),(0,1),(1,0),(-1,0)]
    visited[i][j]=1
    width+=1
    for di in directions:
        dx=j+di[0]
        dy=i+di[1]
        if 0<=dy<m and 0<=dx<n and area[dy][dx]==0 and visited[dy][dx]==0:
            dfs(dy,dx)

numberofarea=0
widthofarea=[]
for i in range(m):
    for j in range(n):
        if area[i][j]==0 and visited[i][j]==0:
            width=0
            dfs(i,j)
            widthofarea.append(width)
            numberofarea+=1

print(numberofarea)
widthofarea=sorted(widthofarea)
for a in widthofarea:
    print(a,end=' ')

