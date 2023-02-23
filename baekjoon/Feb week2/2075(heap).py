# n*n의 표에서 n번째 큰 수를 찾아라
import sys
from heapq import heappush,heappop
n=int(sys.stdin.readline())

#모든 값을 저장해서 sorting하고 n번째 큰 수를 출력하는 방식? -> 메모리 초과 발생
# numbers=[]
# for i in range(n):
#         tmp=list(map(int, sys.stdin.readline().strip().split(' ')))
#         numbers.append(tmp)
# #2차원 배열 -> 1차원 배열로 변환
# numbers=sum(numbers,[])
# numbers.sort(reverse=True)
# print(numbers[n-1])

# 우선순위 큐를 이용해서 한 줄(n개)씩 우선순위 큐에 추가하고, n개 삭제하면서 최종적으로 n번째 큰 수~최대값만 남기는 방식
numbers=[]
for i in range(n):
    tmp=list(map(int, sys.stdin.readline().strip().split(' ')))
    for ele in tmp:
        heappush(numbers, ele)
    while len(numbers)>n:
        heappop(numbers)

print(numbers[0])
