import sys

n=int(sys.stdin.readline())
stairs=[int(sys.stdin.readline()) for _ in range(n)]
stairs.insert(0,0)
if n<=2:
    print(sum(stairs))
    sys.exit(0)

dp=[0]*(n+1)
dp[1]=stairs[1]
dp[2]=stairs[1]+stairs[2]
for i in range(3, n+1):
    dp[i]=max(dp[i-3]+stairs[i-1], dp[i-2])+stairs[i]

print(dp[n])