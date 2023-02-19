# a,b: 땅의 가로,세로
# n : 로봇의 초기 위치 및 방향 개수
# m : 명령의 개수
# L: 로봇이 향하고 있는 방향을 기준으로 왼쪽으로 90도 회전한다.
# R: 로봇이 향하고 있는 방향을 기준으로 오른쪽으로 90도 회전한다.
# F: 로봇이 향하고 있는 방향을 기준으로 앞으로 한 칸 움직인다.
#     n
# w   +   e
#     s
import sys
a,b=map(int, sys.stdin.readline().split(' '))
n,m=map(int,sys.stdin.readline().split(' '))
place=[[0 for _ in range(a+1)] for _ in range(b+1)]
directions=['N','E','S','W']

for i in range(1,n+1):
    x,y,d=sys.stdin.readline().strip().split(' ')
    x=int(x)
    y=int(y)
    place[b-y+1][x]=(i,d)

isTrue=False

for i in range(m):
    robot, command, count=sys.stdin.readline().strip().split(' ');
    robot=int(robot)
    count=int(count)
    x=0
    y=0
    #해당 로봇 위치 찾기
    for k in range(a+1):
        for l in range(b+1):
            if type(place[l][k])==tuple:
                if place[l][k][0]==robot:
                    x=l
                    y=k
                    break
    direction=place[x][y][1]
    if command=='L':
        for c in range(count):
            if direction=='N':
                direction='W'
            elif direction=='E':
                direction='N'
            elif direction=='S':
                direction='E'
            elif direction=='W':
                direction='S'
        place[x][y]=(place[x][y][0],direction)

    elif command=='R':
        for c in range(count):
            if direction == 'N':
                direction = 'E'
            elif direction == 'E':
                direction = 'S'
            elif direction == 'S':
                direction = 'W'
            elif direction == 'W':
                direction = 'N'
        place[x][y] = (place[x][y][0], direction)

    elif command=='F':
        dx=x
        dy=y
        if direction=='N':
            for u in range(count):
                dx = dx - 1
                if 1 <= dx <= b:
                    if place[dx][y] != 0:
                        print('Robot ' + str(robot) + ' crashes into robot ' + str(place[dx][y][0]))
                        isTrue=True
                        sys.exit(0)
                    else:
                        place[dx][y] = place[dx+1][y]
                        place[dx+1][y] = 0
                else:
                    print('Robot ' + str(robot) + ' crashes into the wall')
                    isTrue = True
                    sys.exit(0)
        elif direction=='E':
            for u in range(count):
                dy = dy + 1
                if 1 <= dy <= a:
                    if place[x][dy] != 0:
                        print('Robot ' + str(robot) + ' crashes into robot ' + str(place[x][dy][0]))
                        isTrue = True
                        sys.exit(0)
                    else:
                        place[x][dy] = place[x][dy-1]
                        place[x][dy-1] = 0
                else:
                    print('Robot ' + str(robot) + ' crashes into the wall')
                    isTrue = True
                    sys.exit(0)
        elif direction=='S':
            for u in range(count):
                dx = dx + 1
                if 1 <= dx <= b:
                    if place[dx][y] != 0:
                        print('Robot ' + str(robot) + ' crashes into robot ' + str(place[dx][y][0]))
                        isTrue = True
                        sys.exit(0)
                    else:
                        place[dx][y] = place[dx-1][y]
                        place[dx-1][y] = 0
                else:
                    print('Robot ' + str(robot) + ' crashes into the wall')
                    isTrue = True
                    sys.exit(0)
        elif direction=='W':
            for u in range(count):
                dy = dy - 1
                if 1 <= dy <= a:
                    if place[x][dy] != 0:
                        print('Robot ' + str(robot) + ' crashes into robot ' + str(place[x][dy][0]))
                        isTrue = True
                        sys.exit(0)
                    else:
                        place[x][dy] = place[x][dy+1]
                        place[x][dy+1] = 0
                else:
                    print('Robot ' + str(robot) + ' crashes into the wall')
                    isTrue = True
                    sys.exit(0)

if isTrue==False:
    print('OK')