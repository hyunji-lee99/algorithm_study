n=int(input())
student=list(map(int, input().split(' ')))
b,c=map(int, input().split(' '))

ans=0

for i in range(n):
    # 총 감독관 수를 빼줌
    student[i] -= b
    ans+=1
    # 아직 남아있으면
    if student[i] > 0:
        # 부감독관이 감시할 수 있는 수로 나누어 떨어지면
        # student[i]/c하면 c명을 감독할 수 있는 부감독관이 몇 명이나 필요한지 알 수 있는 것이 포인트
        if student[i]%c==0:
            ans+=student[i]//c
        else:
            ans+=student[i]//c+1


print(ans)

