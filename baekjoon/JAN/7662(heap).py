# 시간초과 발생, heapq 사용해보자
# min heap을 사용하면 원소들이 항상 정렬된 상태로 추가되고 삭제되며, min heap에서 가장 작은 값은
# 항상 인덱스 0, 즉 루트 노드에 위치함.
# t : 입력 테스트 데이터 개수
#      1  ---> root
#    /   \
#   3     5
#  / \   /
# 4   8 7
# min heap에 원소를 추가하는 heappush는 O(log n)
# 원소를 삭제하는 heappop은 원소를 삭제할 대상 리스트를 인자로 넘기면, 가장 작은 원소를 삭제 후에 삭제한 값을 리턴함. O(log n)
# 원소가 들어있는 기존 리스트를 heap으로 변경하려면 heapify를 사용하면 됨. O(n)
# max heap을 만들려면?
# 힙에 튜플 형태로 원소를 추가하거나 삭제함. -> 튜플 내에서 맨 앞에 있는 값을 기준으로 최소 힙이 구성되는 원리 이용
# nums = [4, 1, 7, 3, 8, 5]
# heap = []
#
# for num in nums:
#   heappush(heap, (-num, num))  # (우선 순위, 값)
#
# nsmallest, nlargest 함수가 존재함. -> 주어진 리스트에서 가장 작거나 큰 n개의 값을 담은 리스트를 반환
# 하는데, 그 값의 마지막 값이 가장 작거나 큰 값.
#
# from heapq import nsmallest
#
# nsmallest(3, [4, 1, 7, 3, 8, 5])[-1]

import sys
from heapq import heappush,heappop

t=int(sys.stdin.readline())
for i in range(t):
    minheap=[]
    maxheap=[]
    k=int(sys.stdin.readline())
    exist = [0] * k
    for j in range(k):
        cal,num=sys.stdin.readline().split(' ')
        num=int(num)
        if cal=='I':
            # maxheap, minheap에 존재하는 값인지 체크해줘야 함
            heappush(minheap, (num, j))
            heappush(maxheap, (-num, j))
            #존재하는 값이라는 표시를 visited 배열에 남겨줌
            exist[j]=1
        elif num==1:
            # 반복문을 통해 이미 제거된 정수(exist[j]==0)는 제거
            # maxheap과 minheap을 일종의 동기화해주는 과정
            while maxheap and exist[maxheap[0][1]]==0:
                heappop(maxheap)
            if maxheap:
                exist[maxheap[0][1]] = 0
                heappop(maxheap)
        elif num==-1:
            while minheap and exist[minheap[0][1]]==0:
                heappop(minheap)
            if minheap:
                exist[minheap[0][1]] = 0
                heappop(minheap)
    answer=[]
    if 1 not in exist:
        print('EMPTY')
    else:
        #exist에 남은 원소만
        for node in minheap:
            if exist[node[1]]==1:
                answer.append(node[0])
        print(max(answer),min(answer))



# 평범한 리스트에서 값의 min, max, remove 등을 이용하면 시간복잡도 O(n)인 연산을 최대 10^6번까지 할 수 있어 배열의 크기가 100 이상만 돼도 시간 초과가 발생함.
# for i in range(t):
#     queue=[]
#     # 각 테스트 데이터의 연산 개수
#     k=int(sys.stdin.readline())
#     for j in range(k):
#         cal,num=sys.stdin.readline().split(' ')
#         num=int(num)
#         if cal=='I':
#             queue.append(num)
#         elif cal=='D':
#             if queue:
#                 if num==1:
#                     queue.remove(max(queue))
#                 elif num==-1:
#                     queue.remove(min(queue))
#     if queue:
#         print(max(queue),min(queue))
#     else:
#         print("EMPTY")


