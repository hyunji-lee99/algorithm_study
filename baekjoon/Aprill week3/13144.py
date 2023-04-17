# 시간초과 발생 -> 투 포인터 형식으로 변경하자

import sys

n=int(sys.stdin.readline())
numbers=list(map(int, sys.stdin.readline().split(' ')))

ans=0
en=0
for st in range(n):
    arr=[0]*(100001)
    arr[numbers[st]]=1
    en=st
    while en<n-1 and arr[numbers[en+1]]==0:
        en+=1
        arr[numbers[en]]=1
    ans+=(en-st+1)


print(ans)





