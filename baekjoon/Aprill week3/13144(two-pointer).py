# 시간초과 발생 -> 투 포인터 형식으로 변경 -> 인덱스 짜주는 게 어려웠음. 나중에 다시 풀어보기

import sys

n=int(sys.stdin.readline())
numbers=list(map(int, sys.stdin.readline().split(' ')))

ans=0
en=0
arr = [0] * (100001)
for st in range(n):
    while en<n:
        if arr[numbers[en]]==1:
            break
        arr[numbers[en]] = 1
        en+=1
    ans+=(en-st)
    arr[numbers[st]]=0

print(ans)
