import sys

input=sys.stdin.readline
n,m=map(int, input().split(' '))
# dummy
person=[[0]+list(map(int, input().split(' '))) for _ in range(n)]
person.insert(0, [0]*(m+1))
t=int(input())
target=[list(map(int, input().split(' '))) for _ in range(t)]

# dp[i][j] => dp[1][1]~dp[i][j]까지의 누적합
dp=[x[:] for x in person]
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j]+=(dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1])

for x1,y1,x2,y2 in target:
    print(dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1])
