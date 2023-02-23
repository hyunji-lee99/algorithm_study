#0 : 빈 칸
#1 : 집
#2 : 치킨집
#n : n*n 도시의 사이즈
#m : 폐업시키지 않을 최대 m개 치킨집 수

import sys
from itertools import combinations

n,m=map(int, sys.stdin.readline().split(' '))
map=[]
for i in range(n):
    #map(int, tmp)하면 list object is not callable 에러 발생함
    tmp=sys.stdin.readline().strip().split(' ')
    map.append(tmp)

#치킨집 좌표, 집 좌표 리스트 생성하가
home=[]
chicken=[]
for i in range(n):
    for j in range(n):
        #home
        if map[i][j]=='1':
            home.append((i,j))
        #chicken
        elif map[i][j]=='2':
            chicken.append((i,j))

# itertools에서 제공하는 combination 활용 -> chicken 좌표 리스트에서 m개 선택하는 경우의 수
# m개를 선택하는 경우의 수들 각각의 도시의 치킨거리를 계산해서 최소값 출력
result=1e9
for combi in combinations(chicken,m):
    tmp=0
    for h in home:
        chicken_len=1e9
        for chi in combi:
            chicken_len=min(chicken_len,abs(h[0]-chi[0])+abs(h[1]-chi[1]))
        tmp+=chicken_len
    result=min(result,tmp)

print(result)




