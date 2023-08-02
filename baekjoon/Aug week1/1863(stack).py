import sys

n=int(sys.stdin.readline())

stack=[]
ans=0
for _ in range(n):
    x,y=map(int, sys.stdin.readline().strip().split(' '))
    while stack and stack[-1]>y:
        stack.pop()
        ans+=1
    if y not in stack and y!=0:
        stack.append(y)

if stack:
    ans+=len(stack)

print(ans)