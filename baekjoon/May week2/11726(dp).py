import sys

n=int(sys.stdin.readline())

# 마지막 칸을 1x2로 채웠다면 2x(n-1)를 채우는 경우의 수
# 마지막 칸을 2x1 2개로 채웠다면 2x(n-2)를 채우는 경우의 수
# 2xn을 채우는 경우의 수 dp[n]=dp[n-1]+dp[n-2]
# 피보나치네

dp=[0]*(n+1)
dp[0]=1
dp[1]=1
for i in range(2, n+1):
    dp[i]=(dp[i-1]+dp[i-2])%10007

print(dp[n])