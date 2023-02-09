import sys
from itertools import combinations

n=int(sys.stdin.readline())
numbers=[]
for i in range(n):
    tmp=int(sys.stdin.readline())
    numbers.append(tmp)

#단순히 3개를 itertools combination으로 세 개를 뽑아서 배열 안에 해당하는 합이 있는지 확인하는 방식이라면?
# -> 메모리 초과, 중복인 경우도 적용할 수 없음
# -> 3중 for문으로 푼다면? n이 최대 1000이기 때문에 시간초과 발생
# combi=list(combinations(numbers,3))
# max=0
# for c1,c2,c3 in combi:
#     s=c1+c2+c3
#     if  s in numbers:
#         if max<s:
#             max=s
#
# print(max)

#a+b+c=d == a+b=d-c인 아이디어 이용
#a+b인 배열과 d-c인 배열을 O(n^2)로 찾아주고, a+b=d-c인 배열을 이분탐색으로 찾아줌

#a+b인 배열
ab=[]
for i in numbers:
    for j in numbers:
        ab.append(i+j)
#이분탐색을 위해서 sorting
ab.sort()
#d-c
max=0
for i in numbers:
    for j in numbers:
        dc=i-j
        #자연수만 취급하기 때문에 a+b가 음수가 올 수 없음
        if dc<0:
            continue
        #이분탐색으로 a+b=d-c인 경우 탐색
        start=0
        end=len(ab)-1
        while(start<=end):
            mid=(start+end)//2
            if ab[mid]==dc:
                if max<i:
                    #a+b=d-c이면서 max보다 i(d를 의미함)가 큰 경우
                    max=i
                break
            elif ab[mid]<dc:
                start=mid+1
            elif ab[mid]>dc:
                end=mid-1

print(max)
