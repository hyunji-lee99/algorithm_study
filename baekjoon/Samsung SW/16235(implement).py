n,m,k=map(int, input().split(' '))
# s2d2가 겨울에 뿌리는 양분 배열
A=[list(map(int, input().split(' '))) for _ in range(n)]
# 상도가 심은 나무의 위치 (x,y),나무의 나이 z
trees=[[[] for _ in range(n+1)] for _ in range(n+1)]

# 지문에서 (x,y)라 길래 x를 열(가로), y를 행(세로)라 생각하고 trees[y][x].append(z)로 풀어서 계속 틀렸음
for i in range(m):
    x,y,z=map(int, input().split(' '))
    trees[x][y].append(z)

# 양분 배열 init
feed=[[5]*(n+1) for _ in range(n+1)]

def SpringAndSummer():
    global feed, trees,k
    # 각 나무들이 자신의 양분만큼 양분을 먹고, 나이가 1 증가(같은 칸에 여러 개의 나무가 있을 경우, 나이가 어린 나무부터 양분 먹음)
    # 양분이 부족해서 자신의 나이만큼 양분이 부족하다면 나무는 죽음
    for i in range(1,n+1):
        for j in range(1,n+1):
            if trees[i][j]:
                new_trees = []
                dead = 0
                trees[i][j].sort()
                for year in trees[i][j]:
                    if feed[i][j]-year>=0:
                        feed[i][j]-=year
                        new_trees.append(year+1)
                    else:
                        dead+=year//2
                trees[i][j]=new_trees.copy()
                feed[i][j]+=dead


def AutumnAndWinter():
    global trees
    directions=[(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            feed[i][j]+=A[i-1][j-1]
            if trees[i][j]:
                for year in trees[i][j]:
                    if year%5==0:
                        for di in directions:
                            dy=i+di[1]
                            dx=j+di[0]
                            if 1<=dy<=n and 1<=dx<=n:
                                trees[dy][dx].append(1)

years=1
while years<=k:
    SpringAndSummer()
    AutumnAndWinter()
    years+=1

# 살아남은 나무의 수
numberoftree=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if trees[i][j]:
            numberoftree+=len(trees[i][j])

print(numberoftree)
