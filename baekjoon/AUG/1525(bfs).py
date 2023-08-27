import sys
from collections import deque

target=[['1','2','3'],['4','5','6'],['7','8','0']]
numbers=[list(sys.stdin.readline().strip().split(' ')) for _ in range(3)]

ans=1e9

# DFS는 모든 경로를 탐색해야 해서 최단 경로를 보장하는 BFS로 풀어야 함.
# def dfs(blank,count):
#     global ans, numbers
#     if numbers==target:
#         ans=min(ans, count)
#         return
#     for di in directions:
#         by=blank[0]+di[0]
#         bx=blank[1]+di[1]
#         if 0<=by<3 and 0<=bx<3:
#             numbers[blank[0]][blank[1]]=numbers[by][bx]
#             numbers[by][bx]=0
#             dfs((by,bx),count+1)
#             numbers[by][bx]=numbers[blank[0]][blank[1]]
#             numbers[blank[0]][blank[1]]=0

visited=set()
def bfs(blank, count, numbers):
    global ans
    queue=deque()
    queue.append((blank[0], blank[1], count, numbers))
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    while queue:
        blank_y,blank_x,c,num=queue.popleft()
        if num==target:
            ans=c
            return
        for di in directions:
            by=blank_y+di[0]
            bx=blank_x+di[1]
            if 0<=by<3 and 0<=bx<3:
                new_numbers = [arr[:] for arr in num]
                new_numbers[blank_y][blank_x] = new_numbers[by][bx]
                new_numbers[by][bx]='0'
                str_new_number=''.join(sum(new_numbers,[]))
                if str_new_number not in visited:
                    queue.append((by,bx,c+1, new_numbers))
                    visited.add(str_new_number)

for i in range(3):
    for j in range(3):
        if numbers[i][j]=='0':
            visited.add(''.join(sum(numbers,[])))
            bfs((i,j),0, numbers)
            if ans!=1e9:
                print(ans)
            else:
                print(-1)
            sys.exit(0)


