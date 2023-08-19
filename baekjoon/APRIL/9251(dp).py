import sys

str1='0'+sys.stdin.readline().strip()
str2='0'+sys.stdin.readline().strip()

n=len(str1)
m=len(str2)

dp=[[0]*(n) for _ in range(m)]

for i in range(1,m):
    for j in range(1,n):
        if str2[i]==str1[j]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j], dp[i][j-1])

print(dp[m-1][n-1])
