# 메모리 초과 / 슬라이싱 윈도우 기법을 사용해야 한다고 함
import sys

# 접시의 수, 초밥의 가짓수, 연속해서 먹는 접시의 수, 쿠폰 번호
n,d,k,c=map(int, sys.stdin.readline().split(' '))
sushi=[int(sys.stdin.readline()) for _ in range(n)]

divk=[]
for i in range(n):
    # 범위 안인 경우
    if i+k-1<n:
        divk.append(sushi[i:i+k])
    else:
        front=sushi[i:n]
        back=sushi[:k-len(front)]
        divk.append(front+back)

ans=-1e9
for arr in divk:
    tmp=arr+[c]
    set_arr=list(set(tmp))
    ans=max(ans, len(set_arr))

print(ans)
