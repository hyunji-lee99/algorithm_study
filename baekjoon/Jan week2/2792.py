#n : 아이들의 수
#m : 색상의 수
#이분탐색으로 풀어보자(정답의 범위가 -----++++형식으로 특정 값을 기준으로 나눠지는 경우 사용하는 것을 고려해봐야 함.)

import sys
n,m=map(int,sys.stdin.readline().split(' '))

colors=[]
end=0
for i in range(m):
    color=int(sys.stdin.readline())
    colors.append(color)
    end=max(end,color)

start=1
answer=end
while start<=end:
    mid=(start+end)//2
    #한 명당 나눠주는 보석의 개수가 mid 값일 때, 필요한 사람의 수
    person=0
    for color in colors:
        quote=color//mid
        remain=color%mid
        person+=quote
        if remain>0:
            person+=1

    #사람이 더 필요한 경우 1인당 나눠주는 개수를 더 늘려야 함
    if person>n:
        start=mid+1
    #딱 맞거나 더 필요하지 않은 경우
    else:
        answer=min(answer,mid)
        end=mid-1

print(answer)
