import sys

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())

minimum=[[1e9]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c=map(int, sys.stdin.readline().split(' '))
    # 이미 저장된 경로가 있는 경우, 더 작은 경로를 저장
    if minimum[a][b]!=1e9:
        minimum[a][b]=min(c, minimum[a][b])
    else:
        minimum[a][b]=c

for i in range(1,n+1):
    minimum[i][i]=0

# 1~n까지 경유점 설정해주면서 최소값 탐색
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1, n+1):
            minimum[i][j]=min(minimum[i][j], minimum[i][k]+minimum[k][j])


for i in range(1,n+1):
    for j in range(1, n+1):
        # 도달할 수 있는 경로가 없는 경우
        if minimum[i][j]==1e9:
            print(0, end=' ')
        else:
            print(minimum[i][j], end=' ')
    print('')

