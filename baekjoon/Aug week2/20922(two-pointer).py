import sys

n,k=map(int, sys.stdin.readline().split(' '))
numbers=list(map(int, sys.stdin.readline().split(' ')))

start=0
end=0
count=[0]*100001
ans=-1e9
while end<n:
    if end<n and count[numbers[end]]+1<=k:
        count[numbers[end]]+=1
        end+=1
    else:
        count[numbers[start]]-=1
        start+=1
    ans = max(ans, end - start)

print(ans)
