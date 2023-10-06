import sys
from heapq import heappush, heappop

n=int(sys.stdin.readline())
timetable=[list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]
timetable.sort()

room=[]
# 첫번째 수업의 종료 시간 추가
heappush(room, timetable[0][1])
for i in range(1,n):
    # 힙에서 제일 작은 종료 시간보다 현재 시작 시간이 더 크거나 같으면 가능
    if room[0]<=timetable[i][0]:
        # 현재 가장 작은 종료 시간 업데이트 및 방의 개수 유지
        heappop(room)
        heappush(room, timetable[i][1])
    else:
        # 방 새로 추가
        heappush(room, timetable[i][1])


print(len(room))