#n개의 정수로 이루어진 임의의 수열에서 연속된 몇 개의 수를 선택해서 구할 수 있는 가장 큰 합을 구함. 단, 수는 한 개 이상 선택해야 함
import sys

n=int(sys.stdin.readline())
numbers=list(map(int, sys.stdin.readline().split(' ')))

#n개씩, n-1개씩, n-2개씩,... 연속된 수를 묶어서 저장하고 완전탐색해서 최종 max값을 구하는 방식 -> 시간 초과
# max=-1e9
# for i in range(n,0,-1):
#     for j in range(0,n-i+1):
#         sum_number=sum(numbers[j:j+i])
#         if sum_number>max:
#             max=sum_number
# print(max)

#기존 수열에서 dp 배열의 이전 인덱스 값과 현재 인덱스 값을 더한 값과, 현재 값 중 더 큰 값을 dp 배열에 저장함
#예를 들어,
#numbers=[10,-4,3,1,5,6,-35,12,21,-1]
#dp=[10,6,9,10,15,21,-14,12,33,32]
dp=[0]*n
dp[0]=numbers[0]
for i in range(1,n):
    dp[i]=max(numbers[i],numbers[i]+dp[i-1])

print(max(dp))
