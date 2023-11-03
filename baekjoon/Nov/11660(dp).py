import sys

n,m=map(int, sys.stdin.readline().split(' '))
numbers=[[0]+list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]
numbers.insert(0,[0]*(n+1))
# 각 위치별 부분합 구하기
partSum=[x[:] for x in numbers]
for i in range(1,n+1):
    for j in range(1,n+1):
        partSum[i][j]+=partSum[i][j-1]+partSum[i-1][j]-partSum[i-1][j-1]

for _ in range(m):
    x1,y1,x2,y2=map(int, sys.stdin.readline().split(' '))
    # (x1, y1)과 (x2, y2)까지의 합을 구하라
    ans=partSum[x2][y2]-partSum[x1-1][y2]-partSum[x2][y1-1]+partSum[x1-1][y1-1]
    print(ans)

