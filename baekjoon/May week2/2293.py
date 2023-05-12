# https://velog.io/@jxlhe46/%EB%B0%B1%EC%A4%80-2293%EB%B2%88.-%EB%8F%99%EC%A0%84-1-bfi120m5
# 위 블로그 아이디어 참고
import sys

n,k=map(int, sys.stdin.readline().split(' '))
coin=[int(sys.stdin.readline()) for _ in range(n)]

dp=[[0]*(k+1) for _ in range(n)]
# 첫 번째 동전 한 개만 사용했을 때의 경우의 수 구하기
dp[0][0]=1
for i in range(1, k + 1):
    if i % coin[0] == 0:
        dp[0][i] =1

# dp[i][n]=dp[i-1][n]+dp[i][n-coin]
for i in range(1,n):
    for c in range(0,coin[i]):
        dp[i][c]=dp[i-1][c]
    for j in range(coin[i],k+1):
        dp[i][j]=dp[i-1][j]+dp[i][j-coin[i]]

print(dp[n-1][k])






