#틀렸음 -> 수정중

import sys
#n은 사람 수, t는 술의 총량
n,t=list(map(int,sys.stdin.readline().split(' ')))

people_l=[]
people_r=[]
for i in range(n):
    l,r=list(map(int,sys.stdin.readline().split(' ')))
    people_l.append(l)
    people_r.append(r)

#s값 설정이 불가능한 경우? 모든 사람이 최대 주량으로 마셨지만 t보다 작은 경우, 모든 사람이 최소 주량으로 마셨지만 t보다 큰 경우
if sum(people_r)<t or sum(people_l)>t:
    print(-1)
    sys.exit(0)

#s값 범위 설정(모든 l값보단 크거나 같아야 하고, 모든 r값을 넘어갈 필요는 없으니까)
min_s=max(people_l)
max_s=max(people_r)

#처음엔 모든 사람이 최소값만 마셨다고 가정
t-=sum(people_l)

for s in range(min_s,max_s+1):
    #각 s에 대하여 더 먹을 수 있는 양 계산
    more=0
    for i in range(n):
        if s>people_r[i]:
            more+=(people_r[i]-people_l[i])
        else:
            more+=(s-people_l[i])
    #more 값이 t와 같거나 크다면 만족하는 s (남은 술을 술을 더 마실 수 있는 사람에게 적절하게 나눠주면 되기 때문)
    if more>=t:
        print(more)
        sys.exit(0)

