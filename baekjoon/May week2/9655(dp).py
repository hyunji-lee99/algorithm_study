import sys

n=int(sys.stdin.readline())

# dp[i] : i개의 돌이 있을 때, 돌을 가져가는 횟수
dp=[0]*(n+1)
# n이 1,2,3일 경우 고려
for i in range(1,n+1):
    if i==1:
        dp[1]=1
    elif i==2:
        dp[2]=2
    elif i==3:
        dp[3]=1

for i in range(4, n+1):
    # 3개씩 가져가면 3단계 전 돌을 가져간 횟수 +1
    # 1개씩 가져가면 1단계 전 돌을 가져간 횟수 +1
    dp[i]=min(dp[i-3]+1, dp[i-1]+1)

# 상근이가 먼저 시작하므로, 돌을 가져간 횟수 dp[n]이 홀수이면 상근 승
# 짝수이면 창영 승
if dp[n]%2==0:
    print('CY')
else:
    print('SK')