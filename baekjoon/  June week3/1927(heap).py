import sys
import heapq

# 최소 힙을 이용한 연산
# 배열에 자연수 x를 넣는다.
# 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.

n=int(sys.stdin.readline())
heap=[]
for _ in range(n):
    num=int(sys.stdin.readline())
    # 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거함
    if num==0:
        # heap에 값이 존재하면
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, num)

