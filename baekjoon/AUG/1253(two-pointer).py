import sys

n=int(sys.stdin.readline())
numbers=list(map(int, sys.stdin.readline().strip().split(' ')))
numbers.sort()
ans=0

for idx in range(n):
    start=0
    end=n-2
    value=numbers[idx]
    tmp_numbers=numbers[:idx]+numbers[idx+1:]
    while start<end:
        sum_value=tmp_numbers[start]+tmp_numbers[end]
        if sum_value==value:
            ans+=1
            break
        elif sum_value<value:
            start+=1
        elif sum_value>value:
            end-=1

print(ans)