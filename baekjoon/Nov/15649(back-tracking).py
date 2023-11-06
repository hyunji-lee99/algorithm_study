import sys
from itertools import permutations

n,m=map(int, sys.stdin.readline().split(' '))

# itertools permutaions으로 풀어내는 경우
# nlist=list(range(1,n+1))
# perm=list(permutations(nlist,m))
#
# for p in perm:
#     print(*p, sep=' ')

# dfs를 이용한 백트래킹으로 풀어내는 경우
visited=[0]*(n+1)
arr=[0]*(m)
def dfs(cnt):
    if cnt==m:
        print(*arr, sep=' ')
        return
    for i in range(1,n+1):
        # 아직 방문하지 않은 수인 경우
        if visited[i]==0:
            visited[i]=1
            arr[cnt]=i
            dfs(cnt+1)
            visited[i]=0

dfs(0)

