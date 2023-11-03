import sys

n=int(sys.stdin.readline())
wine=[int(sys.stdin.readline()) for _ in range(n)]

if n<=2:
    print(sum(wine))
    sys.exit(0)

wine.insert(0,0)
dp=[0]*(n+1)
dp[1]=wine[1]
dp[2]=wine[1]+wine[2]
for idx in range(3,n+1):
    # 현재 잔을 마시는 경우의 최댓값
    drink=max(dp[idx-3]+wine[idx-1], dp[idx-2])+wine[idx]
    not_drink=dp[idx-1]
    dp[idx]=max(drink, not_drink)

print(dp[n])
