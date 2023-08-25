import sys
import bisect

n,q=map(int, sys.stdin.readline().split(' '))
numbers=list(map(int, sys.stdin.readline().strip().split(' ')))
numbers.sort()
isExist=[-1]*(numbers[-1]+1)
# setNumbers=set(numbers)
for i in range(n):
    isExist[numbers[i]]=i

for _ in range(q):
    mid=int(sys.stdin.readline().strip())
    if mid>numbers[-1] or isExist[mid]==-1:
        print(0)
    else:
        print(isExist[mid]*(n-isExist[mid]-1))
    # if mid not in setNumbers:
    #     print(0)
    # else:
    #     idx=bisect.bisect_left(numbers,mid)
    #     print(idx*(n-idx-1))



