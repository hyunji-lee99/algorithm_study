import sys

t=int(sys.stdin.readline())
for _ in range(t):
    n=int(sys.stdin.readline())
    if n>3:
        dp = [[0] * (4) for _ in range(n + 1)]
        dp[1][1] = 1
        dp[2][1] = 1
        dp[2][2] = 1
        dp[3][1] = 1
        dp[3][2] = 1
        dp[3][3] = 1
        for i in range(4, n+1):
            dp[i][1]=dp[i-1][1]
            dp[i][2]=dp[i-2][1]+dp[i-2][2]
            dp[i][3]=dp[i-3][1]+dp[i-3][2]+dp[i-3][3]
        print(dp[n][1]+dp[n][2]+dp[n][3])
    else:
        if n==1:
            print(1)
        elif n==2:
            print(2)
        elif n==3:
            print(3)





