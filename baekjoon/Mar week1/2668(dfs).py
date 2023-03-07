# dfs로 탐색해서 자기 자신으로 돌아오는 완전한 사이클을 가진 번호를 찾으면 됨!
import sys

n=int(sys.stdin.readline())
first=[x for x in range(1,n+1)]
second=[]

for i in range(n):
    tmp=int(sys.stdin.readline())
    second.append(tmp)

ans=[]
def dfs(i):
    global target
    if i==target:
        ans.append(i)
    if visited[i-1]==0:
        visited[i - 1] = 1
        dfs(second[i-1])


for i in range(n):
    if first[i]==second[i]:
        ans.append(first[i])
    else:
        visited = [0] * (n)
        target = first[i]
        result = dfs(second[i])


print(len(ans))
for a in ans:
    print(a)
