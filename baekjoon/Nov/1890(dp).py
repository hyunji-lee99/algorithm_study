# https://www.acmicpc.net/board/view/119014 이 문제를 BFS로 풀 수 없는 이유
import sys

n=int(sys.stdin.readline())
step=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]
# 각 위치까지 올 수 있는 경우의 수
dp=[[0]*(n) for _ in range(n)]
dp[0][0]=1
for i in range(n):
    for j in range(n):
        # 0이 아닌 경우, 즉 방문 가능한 칸인 경우
        # step이 0인 경우엔 i+step[i][j], j+step[i][j] 모두 그 자리 그대로인 것으로 계산되어서 현재 위치의 dp값을 더해주기 때문에 계산해선 안된다
        if dp[i][j]!=0 and step[i][j]!=0:
            # 현재 칸에 해당하는 점수만큼 점프해서 dp 값 갱신
            if i+step[i][j]<n:
                dp[i+step[i][j]][j]+=dp[i][j]
            if j+step[i][j]<n:
                dp[i][j+step[i][j]]+=dp[i][j]

print(dp[n-1][n-1])
