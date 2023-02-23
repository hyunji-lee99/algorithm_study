import sys
sys.setrecursionlimit(10**6)

#dfs
sheep=0
wolf=0
def dfs(x,y):
    global sheep
    global wolf
    visited[x][y]=1
    if field[x][y]=='o':
        sheep+=1

    elif field[x][y]=='v':
        wolf+=1

    di=[(1,0),(0,1),(-1,0),(0,-1)]
    for d in di:
        nx=x+d[0]
        ny=y+d[1]
        #범위 안에 들어가면서, 방문한 적이 없고,울타리가 아닌 경우
        if 0<=nx<r and 0<=ny<c and visited[nx][ny]==0 and field[nx][ny]!='#':
            dfs(nx, ny)

r,c=input().split(' ');
r=int(r)
c=int(c)
field=[]
total_sheep=0
total_wolf=0

for i in range(r):
    tmp=input()
    #한글자씩 나누려면 list()로 묶어주면 됨
    field.append(list(tmp))

visited=[[0 for i in range(c)] for j in range(r)]
num_field=0

for i in range(r):
    for j in range(c):
        #방문한 적 없으면서, 울타리가 아닌 경우
        if visited[i][j]==0 and field[i][j]!='#':
            num_field+=1
            sheep=0
            wolf=0
            dfs(i,j)
            if sheep>wolf:
                total_sheep+=sheep
            elif sheep<=wolf:
                total_wolf+=wolf

print(total_sheep, total_wolf)
