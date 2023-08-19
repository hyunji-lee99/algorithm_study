import sys
from itertools import combinations

n=int(sys.stdin.readline())
pos=[list(sys.stdin.readline().strip().split(' ')) for _ in range(n)]

def avoid_teacher(position):
    global n
    directions=[(0,1),(1,0),(-1,0),(0,-1)]
    for i in range(n):
        for j in range(n):
            if position[i][j]=='T':
                # 선생님이면 학생에 도달할 수 있는지 체크
                for dir in directions:
                    dy=i+dir[0]
                    dx=j+dir[1]
                    while 0<=dy<n and 0<=dx<n:
                        # 장애물을 만나면 break
                        if position[dy][dx]=='O':
                            break
                        elif position[dy][dx]=='S':
                            return False
                        dy+=dir[0]
                        dx+=dir[1]
    else:
        return True

object=[]
for i in range(n):
    for j in range(n):
        if pos[i][j]=='X':
            object.append((i,j))
# object 배열에 담긴 후보들 중 3개 선택
nCr=list(combinations(object,3))
for o1,o2,o3 in nCr:
    pos[o1[0]][o1[1]] = 'O'
    pos[o2[0]][o2[1]] = 'O'
    pos[o3[0]][o3[1]] = 'O'
    if avoid_teacher(pos):
        print('YES')
        sys.exit(0)
    pos[o1[0]][o1[1]] = 'X'
    pos[o2[0]][o2[1]] = 'X'
    pos[o3[0]][o3[1]] = 'X'
else:
    print('NO')







