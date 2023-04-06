n,m=map(int, input().split(' '))
center=[list(map(int, input().split(' '))) for _ in range(n)]

# isFinish로 매번 전체 배열 확인해주는 게 아니라, 초기 0의 개수와 탐색된 0의 개수가 같으면 모든 0을 바이러스로 만든 것이므로 카운팅 방식으로 계산해줌
# isFinish로 매번 확인해주면 시간초과 발생했음
init_count_zero = 0
virus=[]
for i in range(n):
    for j in range(n):
        if center[i][j]==2:
            virus.append((i,j))
        elif center[i][j]==0:
            init_count_zero+=1

# virus 배열에서 m개 만큼 뽑는 조합
combinations=[]
def dfs_combination(i,arr):
    global m, virus, combinations
    if len(arr)==m:
        combinations.append(arr)
    for idx in range(i,len(virus)):
        dfs_combination(idx+1, arr+[virus[idx]])


dfs_combination(0,[])

minvalue=1e9
directions=[(0,1),(0,-1),(1,0),(-1,0)]
# 조합으로 m개 만큼 선택하는 경우의 수 완전탐색

# def isFinish(copy_center):
#     for i in range(n):
#         for j in range(n):
#             if copy_center[i][j]==0:
#                 return False
#     return True


for combi in combinations:
   count_zero=0
   copy_center=[arr[:] for arr in center]
   queue=[]
   for y,x in combi:
       queue.append((0,y,x))

   cnt=0
   while queue:
       if init_count_zero==count_zero:
           minvalue = min(cnt, minvalue)
           break

       while queue and queue[0][0]<=cnt:
           time, y,x=queue.pop(0)
           for di in directions:
               dy=y+di[0]
               dx=x+di[1]
               if 0<=dy<n and 0<=dx<n:
                   if copy_center[dy][dx]==0:
                       count_zero+=1
                       copy_center[dy][dx]=3
                       queue.append((time+1, dy, dx))
                   elif copy_center[dy][dx]==2:
                       copy_center[dy][dx] = 3
                       queue.append((time + 1, dy, dx))

       cnt+=1

if minvalue==1e9:
    print(-1)
else:
    print(minvalue)




