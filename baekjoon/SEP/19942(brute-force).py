import sys
from itertools import combinations

n=int(sys.stdin.readline())
p,f,s,v=map(int, sys.stdin.readline().strip().split(' '))
nutri=[]
for _ in range(n):
    nutri.append(list(map(int, sys.stdin.readline().strip().split(' '))))

numbers=list(range(1,n+1))
min_cost=1e9
min_idx={}

for pick in range(1,n+1):
    pick_idx=list(combinations(numbers, pick))
    isAllPass=True
    for picked in pick_idx:
        mp, mf, ms, mv = 0, 0, 0, 0
        tmp_cost = 0
        for idx in picked:
            mp+=nutri[idx-1][0]
            mf+=nutri[idx-1][1]
            ms+=nutri[idx-1][2]
            mv+=nutri[idx-1][3]
            tmp_cost+=nutri[idx-1][4]
        if mp >= p and mf >= f and ms >= s and mv >= v:
            if min_cost >= tmp_cost:
                min_cost = tmp_cost
                if min_cost in min_idx.keys():
                    min_idx[min_cost].append(picked)
                else:
                    min_idx[min_cost]=[]
                    min_idx[min_cost].append(picked)
        else:
            isAllPass = False

    # 모든 인덱스를 뽑는 경우의 수가 조건을 만족할 때 더 큰 값은 탐색할 필요없음
    if isAllPass:
        break

if min_cost==1e9:
    print(-1)
else:
    print(min_cost)
    min_idx[min_cost].sort()
    print(*min_idx[min_cost][0], sep=' ')

