import sys
input=sys.stdin.readline

n=int(input())
eggs=[]
for _ in range(n):
    d,w=map(int, input().split(' '))
    eggs.append([d,w])

answer=-1e9
# num은 현재 들고 있는 계란 번호
# cnt는 깨진 계란 수
def backtracking_eggs(num, cnt):
    global answer
    if num==n:
        # 마지막 계란까지 모두 탐색한 경우
        answer=max(answer, cnt)
        return
    # num번 계란이 이미 깨져있다면 다음 계란으로 넘어감
    if eggs[num][0] <= 0 or cnt==n-1:
        backtracking_eggs(num+1, cnt)
        return

    for i in range(n):
        if i==num:
            # 현재 들고 있는 계란인 경우 넘어감
            continue
        # i번 계란이 현재 깨진 상태면 넘어감
        if eggs[i][0]<=0:
            continue
        # num번 계란과 i번 계란 부딪히는 경우
        tmp=cnt
        eggs[num][0] -= eggs[i][1]
        eggs[i][0] -= eggs[num][1]
        if eggs[num][0]<=0:
            cnt+=1
        if eggs[i][0]<=0:
            cnt+=1
        backtracking_eggs(num+1, cnt)
        eggs[num][0] += eggs[i][1]
        eggs[i][0] += eggs[num][1]
        cnt=tmp


backtracking_eggs(0,0)

print(answer)




