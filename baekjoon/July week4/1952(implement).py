import sys

m,n=map(int, sys.stdin.readline().split(' '))
# 북 동 남 서
# y x
directions=[(-1,0),(0,1),(1,0),(0,-1)]
visited=[[0]*(n) for _ in range(m)]
visited[0][0]=1
visited_num=1
curx, cury=0,0
dir=1
ans=0
while visited_num<m*n:
    new_x = curx + directions[dir][1]
    new_y=cury+directions[dir][0]
    if 0<=new_x<n and 0<=new_y<m and visited[new_y][new_x]==0:
        visited[new_y][new_x]=1
        visited_num+=1
        curx=new_x
        cury=new_y
    else:
        dir=(dir+1)%4
        ans+=1

print(ans)
