import sys
import heapq

n=int(sys.stdin.readline())
times=[]
for _ in range(n):
    start, end=map(int, sys.stdin.readline().split(' '))
    times.append([start, end])
# 시작 시간 순으로 정렬
times.sort(key=lambda x:x[0])
# 사용가능한 회의실
rooms=[]
for start, end in times:
    # heap의 제일 작은 값이 현재 start 값보다 작거나 같으면
    if rooms and rooms[0]<=start:
        heapq.heappop(rooms)
    heapq.heappush(rooms, end)

print(len(rooms))
