import sys

n,m=map(int, sys.stdin.readline().split(' '))
nlist=list(map(int, sys.stdin.readline().split(' ')))

nlist.sort()

arr=[0]*m
ans=set()
def dfs(cnt, num):
    if cnt==m:
        ans.add(' '.join(map(str, arr)))
        return

    for i in range(num, n):
        arr[cnt]=nlist[i]
        dfs(cnt+1, i)

dfs(0,0)

for s in sorted(ans, key=lambda x:list(map(int, x.split(' ')))):
    print(s)
