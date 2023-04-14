import sys

n, m = map(int, sys.stdin.readline().split(' '))

# init
rooms = dict()
for i in range(n):
    name = sys.stdin.readline().strip()
    rooms[name] = [0] * 18

for j in range(m):
    name, start, end = sys.stdin.readline().strip().split(' ')
    start = int(start)
    end = int(end)
    for t in range(start, end):
        rooms[name][t] = 1

rooms=dict(sorted(rooms.items()))
last=list(rooms.keys())[-1]

for name, time in rooms.items():
    print('Room ' + name + ':')
    times = []
    # 빈자리가 없을 경우
    if 0 not in time[9:]:
        print('Not available')
    # 빈 자리가 있을 경우
    else:
        tmp = []
        for i in range(9, 18):
            if time[i] == 0:
                if i==17:
                    tmp.append(i)
                    times.append(tmp)
                else:
                    tmp.append(i)
            else:
                if tmp:
                    times.append(tmp)
                    tmp = []
        print(str(len(times))+' available:')
        for t in times:
            if t[0]==9:
                print('09',end='')
            else:
                print(str(t[0]), end='')
            print('-'+str(t[-1]+1))

    if name!=last:
        print('-----')





