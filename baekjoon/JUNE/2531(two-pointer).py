
import sys

# 접시의 수, 초밥의 가짓수, 연속해서 먹는 접시의 수, 쿠폰 번호
n,d,k,c=map(int, sys.stdin.readline().split(' '))
sushi=[int(sys.stdin.readline()) for _ in range(n)]

# k개씩 초밥을 묶어서 모든 경우의 수를 완전 탐색하면 최악의 경우, 30000개를 모두 슬라이싱하고, set으로 중복을 제거해주는 과정에서 메모리 초과 / 시간 초과 발생함
# slicing window 기법을 사용해야 함.
# divk=[]
# for i in range(n):
#     # 범위 안인 경우
#     if i+k-1<n:
#         divk.append(sushi[i:i+k])
#     else:
#         front=sushi[i:n]
#         back=sushi[:k-len(front)]
#         divk.append(front+back)
#
# ans=-1e9
# for arr in divk:
#     tmp=arr+[c]
#     set_arr=list(set(tmp))
#     ans=max(ans, len(set_arr))
#
# print(ans)

# slicing window
left, right=0,0
ans=0
while left<=n:
    right=left+k
    window=set()
    # c번 스시 있는지 확인
    existC=False
    for i in range(left, right):
        i=i%n
        window.add(sushi[i])
        if sushi[i]==c:
            existC=True
    cnt=len(window)
    # c번 스시가 없다면
    if not existC:
        cnt+=1
    ans=max(ans, cnt)
    left+=1

print(ans)







