import sys

n,d=map(int, sys.stdin.readline().split(' '))
graph=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]
dp=[1e9]*(d+1)
dp[0]=0

for i in range(d+1):
    # dp[i]로 값을 먼저 채우고 최솟값인지 탐색해줘야 함
    dp[i]=min(dp[i], dp[i-1]+1)
    for s,e,w in graph:
        if i==s and e<=d and dp[s]+w<dp[e]:
            dp[e]=dp[s]+w



print(dp[d])
