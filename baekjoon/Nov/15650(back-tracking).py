import sys

n,m=map(int, sys.stdin.readline().split(' '))

# 1~n 까지의 자연수 중 m개를 고른 수열, 고른 수열은 오름차순이어야 함
visited=[0]*(n+1)
arr=[0]*(m)
def dfs(cnt, num):
    if cnt==m:
        print(*arr, sep=' ')
        return
    for i in range(num+1, n+1):
        if visited[i]==0:
            visited[i]=1
            arr[cnt]=i
            dfs(cnt+1, i)
            visited[i]=0

dfs(0,0)
