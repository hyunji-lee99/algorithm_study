import sys

input=sys.stdin.readline

n=int(input())
meeting=[]
for _ in range(n):
    s,e=map(int, input().split(' '))
    meeting.append([s,e])

meeting.sort(key=lambda x:(x[1],x[0]))

cur_endtime=meeting[0][1]
answer=1
for i in range(1,n):
    # 현재 회의의 종료 시간이 다음 회의 시작 시간보다 작거나 같다면 가능
    if cur_endtime<=meeting[i][0]:
        cur_endtime=meeting[i][1]
        answer+=1

print(answer)