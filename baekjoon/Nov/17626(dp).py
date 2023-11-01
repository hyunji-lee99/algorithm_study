import sys
import math

n=int(sys.stdin.readline())
dp=[0]*(n+1)
for i in range(1,n+1):
    # 현재 수에서 제곱근의 정수부분만 제곱한 값을 뺀 나머지의 가장 작은 항의 수 +1
    # 이 방법은 틀렸다! 예를 들어, 23의 경우 16+4+1+1+1 보다 9+9+4+1이 항의 개수가 더 작다
    # dp[i]=dp[i-pow(int(math.sqrt(i)),2)]+1

    # i보다 더 작은 제곱수들을 모두 구한 뒤에, 해당 dp[i-제곱수] 값이 가장 작은 것에 +1해줘야 답을 구할 수 있다.
    min_value=1e9
    j=1
    while j*j<=i:
        min_value=min(dp[i-j*j],min_value)
        j+=1
    dp[i]=min_value+1

print(dp[n])
