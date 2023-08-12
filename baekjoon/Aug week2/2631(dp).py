import sys
# 2<=n<=200
n=int(sys.stdin.readline())
line=[int(sys.stdin.readline()) for _ in range(n)]

# 가장 큰 증가하는 부분 수열을 구해서 전체 길이에서 빼주면 된다.
dp=[1]*(n)
for idx in range(n):
    for j in range(idx):
        if line[j]<line[idx]:
            dp[idx]=max(dp[j]+1, dp[idx])
print(n-max(dp))