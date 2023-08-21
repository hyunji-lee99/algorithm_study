# 규칙찾아서 점화식 만들어서 푸는 DP?
# 1)
# N=1:1 N=2:3 N=3:3 N=4:8 N=5:13
# N=4부터 DP[N]=DP[N-2]+DP[N-1]+2 인가?
# 아님! 결과만 보고 결정하지 말고, 원리를 도출해서 생각해내자 => 결과만 보고 점화식이 바로 도출되는 경우는 함정일 수 있음

# 2)
# https://stillchobo.tistory.com/106
# 좌우대칭을 신경쓰지 않으면 dp[n]=dp[n-1]+dp[n-2]*2 지만, 좌우대칭을 신경쓰면
# 2가지 경우의 좌우대칭이 있음
# 1. 원래 자체적으로 좌우대칭인 모양
# 2. 뒤집으면 좌우대칭이 되는 모양
# dp[n]=1번+2번인 상태이므로 2번의 경우를 /2해서 1가지로 취급해줘야 함 => 답=1번+(2번/2)
# 여기서, dp[n]=1번+2번이므로 2번=dp[n]-1번 => 답=(dp[n]+1번)/2
# 이제 1번인 경우의 수를 구하려면 n이 홀수인 경우, 중간에 반드시 1*2(세로)모양이 와야 하므로, dp[(n-1)/2]
# n이 짝수인 경우 dp[n/2]와 중간에 2*2와 2*1이 들어가는 모양이므로 dp[n/2-1]*2
# => n이 홀수인 경우엔, (dp[n]+dp[(n-1)/2])/2
# => n이 짝수인 경우엔, (dp[n]+dp[n/2]+dp[n/2-1]*2)/2

import sys

n=int(sys.stdin.readline())

dp=[0]*(n+1)
dp[0]=1
dp[1]=1
# 좌우대칭이 모두 포함된 DP배열을 만들어보면
for i in range(2, n+1):
    dp[i]=dp[i-1]+dp[i-2]*2

# 좌우대칭인 경우를 모두 제거한 답
if n%2==1:
    ans=(dp[n]+dp[(n-1)//2])/2
else:
    ans=(dp[n]+dp[n//2]+dp[n//2-1]*2)/2

print(int(ans))


