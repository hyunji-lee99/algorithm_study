import sys

n=int(sys.stdin.readline())
# dp[i] : 정수 i를 1로 만들 수 있는 최소 연산 횟수
dp=[0]*(n+1)
dp[1]=0
for i in range(2, n+1):
    # 3과 2의 공배수인 경우
    if i%3==0 and i%2==0:
        dp[i]=min(dp[i//3]+1, dp[i//2]+1, dp[i-1]+1)
    elif i%3==0:
        dp[i]=min(dp[i//3]+1, dp[i-1]+1)
    elif i%2==0:
        dp[i]=min(dp[i//2]+1, dp[i-1]+1)
    else:
        dp[i]=dp[i-1]+1

print(dp[n])