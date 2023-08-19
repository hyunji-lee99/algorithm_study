import sys

n=int(sys.stdin.readline())
top=list(map(int,sys.stdin.readline().strip().split(' ')))

ans=[0]*n
stack=[]

for i in range(1,n+1):
    cur=top[i-1]
    while stack and stack[-1][0]<cur:
        stack.pop()
    if stack:
        ans[i-1]=stack[-1][1]
    stack.append([cur, i])

for a in ans:
    print(a, end=' ')


