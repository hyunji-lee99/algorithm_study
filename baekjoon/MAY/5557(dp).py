import sys
from collections import deque

n=int(sys.stdin.readline())
numbers=list(map(int, sys.stdin.readline().split(' ')))
# 앞쪽 n-1개 수로 +,-를 이용해서 만들어야 하는 수
equal=numbers.pop()
# 중간에 계산결과는 0 이상 20 이하

# bfs를 이용? -> 시간초과 발생함(2^(n-2)까지 완전 탐색해야 하기 때문에, n<=100이므로 2^98를 탐색할 경우 시간 초과)
# queue=deque()
# queue.append((numbers.pop(0),0))
# index=0
# while index<n-2:
#     while queue and queue[0][1]<=index:
#         cur, idx = queue.popleft()
#         for temp in (cur + numbers[idx], cur - numbers[idx]):
#             if 0 <= temp <= 20:
#                 queue.append((temp, idx + 1))
#     index+=1
#
# ans=0
# for value, idx in queue:
#     if value==equal:
#         ans+=1

# dp를 이용하자
# dp 정의 : dp[i][j]=k
# i번째 숫자까지 탐색했을 때, j를 만들 수 있는 경우의 수는 k개
dp=[[0]*(21) for _ in range(n-1)]
# 0번째 숫자까지 탐색했을 때 만들 수 있는 수는 numbers[0]
dp[0][numbers[0]]=1

for i in range(1,n-1):
    for j in range(21):
        if dp[i-1][j]:
            if 0<=j+numbers[i]<=20:
                dp[i][j+numbers[i]]+=dp[i-1][j]
            if 0<=j-numbers[i]<=20:
                dp[i][j-numbers[i]]+=dp[i-1][j]

print(dp[n-2][equal])
