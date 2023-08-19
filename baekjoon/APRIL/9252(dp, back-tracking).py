# 다시 풀어보기 -> 정답보고 이해했음
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

si=m-1
sj=n-1
ans=[]

#백트래킹
while si!=0 and sj!=0:
    if str1[sj]==str2[si]:
        ans.append(str2[si])
        si-=1
        sj-=1
    else:
        if dp[si-1][sj]==dp[si][sj]:
            si-=1
        elif dp[si][sj-1]==dp[si][sj]:
            sj-=1

for s in range(len(ans)-1,-1,-1):
    print(ans[s], end='')