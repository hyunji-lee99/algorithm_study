import sys

n=int(sys.stdin.readline())
energy=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(n-1)]
k=int(sys.stdin.readline())

# n번째 돌까지 왔을 때 드는 최소 에너지
dp=[[1e9]*(2) for _ in range(n)]
dp[0][0]=0
dp[0][1]=0
for i in range(1,n):
    # 작은 점프를 할 수 있는 경우
    # 매우 큰 점프를 사용하지않은 경우
    dp[i][0]=min(dp[i-1][0]+energy[i-1][0], dp[i][0])
    # 매우 큰 점프를 사용한 경우
    dp[i][1]=min(dp[i-1][1]+energy[i-1][0], dp[i][1])
    if i>=2:
        # 큰 점프를 할 수 있는 경우
        dp[i][0] = min(dp[i - 2][0] + energy[i - 2][1],dp[i][0])
        dp[i][1] = min(dp[i - 2][1] + energy[i - 2][1], dp[i][1])
    if i>=3:
        # 매우 큰 점프를 할 수 있는 경우(단 한 번만 가능)
        dp[i][1] = min(dp[i - 3][0] + k, dp[i][1])

print(min(dp[n-1][0], dp[n-1][1]))


