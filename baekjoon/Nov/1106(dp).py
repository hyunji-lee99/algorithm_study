import sys

input=sys.stdin.readline
c,n=map(int, input().split(' '))
# 비용 / 사람 수
info=[list(map(int, input().split(' '))) for _ in range(n)]

# info로 입력 될 수 있는 최대 사람 수가 100명이고, c보다 더 많은 사람에게 홍보할 수 있는 비용이 최솟값일 수 있음
dp=[1e9]*(c+100)
dp[0]=0
for cost, people in info:
    for i in range(people, c+100):
        dp[i]=min(dp[i-people]+cost, dp[i])

print(min(dp[c:]))