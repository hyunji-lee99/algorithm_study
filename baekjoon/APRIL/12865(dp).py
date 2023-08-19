import sys

n,k=map(int, sys.stdin.readline().split(' '))
# w,v
things=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]
things.insert(0,[0,0])

# # 무게가 k 이하인 조합 뽑아내기
# combinations=[]
# def combination(idx,arr):
#     if arr:
#         combinations.append(arr)
#     for i in range(idx, len(things)):
#         sumarr=arr+[things[i]]
#         weight=[a[0] for a in sumarr]
#         if sum(weight)<=k:
#             combination(i+1, sumarr)
#
# combination(0,[])
#
# maxvalue=-1e9
# for combi in combinations:
#     value=sum([a[1] for a in combi])
#     maxvalue=max(maxvalue, value)
#
# print(maxvalue)
# -> 시간초과 발생 -> DP로 풀어보자!

#dummy
dp=[[0]*(k+1) for _ in range(n+1)]
# dp[n][k]는 n번째 물건까지 살펴보았을 때, 무게가 k인 배낭의 최대 가치
for i in range(1,n+1): # 물건 인덱스
    for j in range(1,k+1): # 현재 가방 가능한 무게
        weight=things[i][0]
        value=things[i][1]
        # 현재 가방 무게보다 무겁다면, 이전 물건의 현재 가방 무게의 최대 가치를 저장함
        if weight>j:
            dp[i][j]=dp[i-1][j]
        # 아니라면, 해당 물건을 넣을지 뺄지 결정
        # 이전 물건까지 살펴봤을 때, (현재 가방 무게 - 현재 물건 무게)인 배낭의 최대가치에 현재 물건 가치를 더한 값과
        # 이전 물건까지 살펴봤을 때의 현재 가방무게에서 최대가치 값을 비교해서 더 큰 값을 넣어줌
        else:
            dp[i][j]=max(dp[i-1][j-weight]+value, dp[i-1][j])

print(dp[n][k])




