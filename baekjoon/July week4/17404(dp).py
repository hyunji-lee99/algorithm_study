import sys
from collections import deque

n=int(sys.stdin.readline())
# 빨강 초록 파랑 칠하는 비용
cost=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]

# 시간초과 코드(bfs)
# 1번 집을 빨, 초, 파로 칠하는 경우
# 빨=0, 초=1, 파=2
# minvalue=1e9
# for one in range(3):
#     # 컬러 값과 비용과 인덱스 저장
#     queue=deque()
#     queue.append((one, cost[0][one], 0))
#     while queue:
#         cur_color, cur_cost, cur_idx =queue.popleft()
#         if cur_idx==n-1:
#             minvalue=min(cur_cost, minvalue)
#         elif cur_idx==n-2:
#             for new_color in range(3):
#                 if new_color!=one and new_color!=cur_color:
#                     queue.append((new_color, cur_cost+cost[cur_idx+1][new_color], cur_idx+1))
#         else:
#             for new_color in range(3):
#                 if new_color!=cur_color:
#                     queue.append((new_color, cur_cost+cost[cur_idx+1][new_color], cur_idx+1))
#
# print(minvalue)

# dp를 이용해서 풀어보자
# 빨=0, 초=1, 파=2
ans=1e9
for i in range(3):
    dp=[[1e9, 1e9, 1e9] for _ in range(n)]
    dp[0][i]=cost[0][i]
    for j in range(1, n):
        dp[j][0]=cost[j][0]+min(dp[j-1][1], dp[j-1][2])
        dp[j][1]=cost[j][1]+min(dp[j-1][0], dp[j-1][2])
        dp[j][2]=cost[j][2]+min(dp[j-1][0], dp[j-1][1])
    for c in range(3):
        if c!=i:
            ans=min(ans, dp[n-1][c])

print(ans)