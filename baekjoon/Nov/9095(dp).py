import sys

t=int(sys.stdin.readline())
for _ in range(t):
    n=int(sys.stdin.readline())
    # dp[0]=0, dp[1]=1 ('1'), dp[2]=2 ('2','1+1'), dp[3]=4 ('3','1+2','2+1','1+1+1')
    dp = [0, 1, 2, 4]
    for i in range(4, n + 1):
        dp.append(dp[i - 3] + dp[i - 2] + dp[i - 1])
    print(dp[n])
