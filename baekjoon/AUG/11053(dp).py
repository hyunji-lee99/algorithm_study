import sys

n=int(sys.stdin.readline())
numbers=list(map(int, sys.stdin.readline().split(' ')))

dp=[1]*n
for idx in range(n):
    for j in range(idx):
        if numbers[j]<numbers[idx]:
            dp[idx]=max(dp[idx], dp[j]+1)

print(max(dp))