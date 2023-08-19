import sys

# 방의 개수 n, 용사의 초기공격력 atk
n,atk=map(int, sys.stdin.readline().split(' '))
# 각 방의 정보
rooms=[list(map(int,sys.stdin.readline().split(' '))) for _ in range(n)]

# 1e9 -> int(1e9)로 바꿔주니까 시간초과 해결.
minHP=int(1e18)
start=1
end=int(1e18)
while start<=end:
    mid=(start+end)//2
    # 해당 mid값으로 n번방 용까지 무찌를 수 있는지 확인
    flag=True
    cur_atk=atk
    cur_hp=mid

    for t,a,h in rooms:
        # 통과하지 못하는 방이 있을 경우
        if flag==False:
            break
        # 몬스터가 있을 경우
        if t==1:
            # while 반복문은 시간초과
            # while True:
            #     # 몬스터의 생명력에서 용사의 공격력만큼 뺌
            #     # 몬스터가 사망하면
            #     if h - cur_atk <= 0:
            #         break
            #     # 몬스터가 사망하지 않으면
            #     else:
            #         h-=cur_atk
            #     # 용사의 생명력에서 몬스터의 공격력만큼 뺌
            #     # 용사가 사망하면
            #     if cur_hp-a<=0:
            #         flag=False
            #         break
            #     else:
            #         cur_hp-=a

            # 몬스터를 업애기 위해 필요한 공격횟수 cnt 계산
            if h%cur_atk==0:
                cnt=h//cur_atk
            else:
                cnt=h//cur_atk+1
            # 용사가 먼저 때리기 때문에, 몬스터를 업애기 전에 용사가 사망하는지 확인
            # 몬스터 hp 감소
            # 용사 hp 감소순이니까
            # 몬스터를 업애기 전에 용사 hp가 0보다 작거나 같아지지 않는지 확인
            cur_hp-=a*(cnt-1)
            if cur_hp<=0:
                flag=False

        elif t==2:
            cur_hp=min(cur_hp+h, mid)
            cur_atk+=a
    # 통과가 가능한 경우, 더 작은 mid값으로 통과할 수 있는지 확인
    if flag==True:
        minHP=mid
        end=mid-1
    # 통과가 불가능한 경우, 더 큰 mid값으로 변경해줘야 함
    elif flag==False:
        start=mid+1

print(minHP)
