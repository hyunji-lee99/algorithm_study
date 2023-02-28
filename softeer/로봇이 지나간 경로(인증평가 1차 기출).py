import sys
from collections import deque

h, w = map(int, sys.stdin.readline().split(' '))

map = []
for i in range(h):
    tmp = list(sys.stdin.readline().strip())
    map.append(tmp)

direction = [(0, 1),(1, 0),(0, -1),(-1, 0)]
directions=['>','v','<','^']

def check(i, j):
    cnt = 0
    for di in range(4):
        dy = i + direction[di][0]
        dx = j + direction[di][1]
        if 0 <= dy < h and 0 <= dx < w and map[dy][dx]=='#':
            cnt += 1
    if cnt > 1:
        return False
    return True

def bfs(i,j):
    queue=deque()
    queue.append((i,j))
    visitied=[[0]*w for _ in range(h)]
    path=deque()
    while queue:
        curi,curj=queue.popleft()
        visitied[curi][curj]=1
        for di in range(4):
            dy = curi + direction[di][0]
            dx = curj + direction[di][1]
            if 0 <= dy < h and 0 <= dx < w and map[dy][dx] == '#' and visitied[dy][dx]==0:
                queue.append((dy,dx))
                path.append(directions[di])

    return path



for i in range(h):
    for j in range(w):
        if map[i][j] == '#' and check(i, j):
            answer = []
            #bfs로 탐색 시작
            path=bfs(i,j)
            print(i+1,j+1)
            print(path[0])
            cur=path.popleft()
            cnt = 1
            for next in path:
                if cur==next:
                    cnt+=1
                    cur=next
                    if cnt%2==0:
                        answer.append('A')
                        cnt=0
                #index가 1 감소했을 때와 동일하면, 왼쪽으로 회전한 것
                elif directions[directions.index(cur)-1]==next:
                    answer.append('L')
                    cur=next
                    cnt+=1
                # index가 1 증가했을 때와 동일하면, 오른쪽으로 회전한 것
                else:
                    answer.append('R')
                    cur=next
                    cnt+=1

            for ans in answer:
                print(ans,end="")
            sys.exit(0)
